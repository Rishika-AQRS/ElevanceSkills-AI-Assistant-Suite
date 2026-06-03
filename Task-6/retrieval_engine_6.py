import os
import pickle
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer

class RetrievalEngine:
    def __init__(self, artifacts_dir="artifacts"):
        index_path=f"{artifacts_dir}/support.index"
        csv_path=f"{artifacts_dir}/support_faq.csv"
        meta_path=f"{artifacts_dir}/metadata.pkl"

        if not os.path.exists(index_path) or not os.path.exists(csv_path) or not os.path.exists(meta_path):
            raise FileNotFoundError("Artifacts not found. Run `python data_build.py` first.")

        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.index=faiss.read_index(index_path)
        self.df=pd.read_csv(csv_path)
        with open(meta_path, "rb") as f:
            self.meta=pickle.load(f)

    def search(self, query, top_k=3):
        qvec=self.model.encode([query], convert_to_numpy=True, normalize_embeddings=True).astype("float32")
        scores, idxs=self.index.search(qvec, top_k)

        results=[]
        for score, idx in zip(scores[0], idxs[0]):
            if idx==-1:
                continue
            item = self.meta[idx]
            results.append({
                "instruction": item.get("instruction", ""),
                "response": item.get("response", ""),
                "intent": item.get("intent", ""),
                "category": item.get("category", ""),
                "score": float(score)
            })
        return results