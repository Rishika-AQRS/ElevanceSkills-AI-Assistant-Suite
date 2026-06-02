import faiss
import pickle
import os
import pandas as pd
from datasets import load_dataset
from sentence_transformers import SentenceTransformer

OUT_DIR="artifacts"
os.makedirs(OUT_DIR, exist_ok=True)

dataset=load_dataset("bitext/Bitext-customer-support-llm-chatbot-training-dataset")
split_name="train" if "train" in dataset else list(dataset.keys())[0]
ds=dataset[split_name]

required_cols=["instruction", "response"]
for col in required_cols:
    if col not in ds.column_names:
        raise ValueError(f"Missing required columns: {col}. Found: {ds.column_names}")
rows=[]
for item in ds:
    instruction=str(item["instruction"]).strip()
    response=str(item["response"]).strip()
    intent=str(item["intent"]).strip() if "intent" in ds.column_names else ""
    category = str(item["category"]).strip() if "category" in ds.column_names else ""
    if instruction and response:
        rows.append({
            "instruction":instruction,
            "response":response,
            "intent":intent,
            "category":category
        }) 

df=pd.DataFrame(rows).drop_duplicates(subset=["instruction", "response"]).reset_index(drop=True)
df.to_csv(f"{OUT_DIR}/support_faq.csv", index=False)

model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
embeddings=model.encode(
    df["instruction"].tolist(),convert_to_numpy=True,
    show_progress_bar=True,
    normalize_embeddings=True
)

index=faiss.IndexFlatIP(embeddings.shape[1])

index.add(embeddings.astype("float32"))

faiss.write_index(index, f"{OUT_DIR}/support.index")

with open(f"{OUT_DIR}/metadata.pkl", "wb") as f:
    pickle.dump(df.to_dict("records"), f)

print(f"Build completed sucessfully! Saved {len(df)} rows to {OUT_DIR}/")
