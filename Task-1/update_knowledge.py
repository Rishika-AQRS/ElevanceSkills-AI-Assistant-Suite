# Task-1/update_knowledge.py

import os
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
BASE_DIR=os.path.dirname(os.path.abspath(__file__))

SOURCE_DIR=os.path.join(BASE_DIR, "sources")
VSTORE_DIR=os.path.join(BASE_DIR, "embeddings", "faiss")
def main():
    print("\n" + "=" * 60)
    print("📚 CREATING KNOWLEDGE BASE")
    print("=" * 60)
    
    print("\n[1/4] Loading SentenceTransformer model...")
    model=SentenceTransformer("all-MiniLM-L6-v2")
    print("✅ Model loaded!")
    
    print(f"\n[2/4] Reading files from sources/...")
    print(f"📁 Looking in: {SOURCE_DIR}")
    texts=[]
    
    if not os.path.exists(SOURCE_DIR):
        print(f"❌ Error: Folder 'sources' not found at {SOURCE_DIR}")
        return
    
    files=sorted([f for f in os.listdir(SOURCE_DIR) if f.endswith(".txt")])
    
    if not files:
        print("❌ Error: No .txt files found in sources/")
        return
    
    for fname in files:
        with open(os.path.join(SOURCE_DIR, fname), "r", encoding="utf-8") as f:
            content=f.read().strip()
            if content:
                texts.append(content)
                print(f"   ✅ Loaded: {fname}")
    
    print(f"\n✅ Found {len(files)} file(s)")
    
    print("\n[3/4] Splitting into chunks...")
    splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents=splitter.create_documents(texts)
    print(f"✅ Created {len(documents)} chunks")
    
    print("\n[4/4] Creating FAISS vector store...")
    os.makedirs(VSTORE_DIR, exist_ok=True)
    embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

    db=FAISS.from_documents(documents, embeddings)
    db.save_local(VSTORE_DIR)
    
    print("\n" + "=" * 60)
    print("✅ KNOWLEDGE BASE CREATED!")
    print(f"📁 Saved to: {os.path.abspath(VSTORE_DIR)}")
    print("=" * 60)

if __name__ == "__main__":
    main()
