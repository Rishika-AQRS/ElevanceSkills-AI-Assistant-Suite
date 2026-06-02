import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import os

print("Loading Data....")
df=pd.read_csv('Task-4/data/arxiv_subset/ai_papers.csv')

abstracts=df['abstract'].fillna("").head(500).tolist()
df=df.head(500)

model=SentenceTransformer('all-MiniLM-L6-v2')

embeddings=model.encode(abstracts)
dimension=embeddings.shape[1]
index=faiss.IndexFlatL2(dimension)
index.add(embeddings.astype('float32'))

os.makedirs('Task-4/vector_db', exist_ok=True)
faiss.write_index(index, 'Task-4/data/vector_db/arxv_papers.index')
df.to_pickle('Task-4/data/vector_db/papers_metadata.pk1')

print("Success! 'arxiv_paper.index' and 'papers_metadata.pk1' are saved in 'Task-4/data/vector_db/'." )