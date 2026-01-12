import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings 

# 1. Load Environment Variables
load_dotenv()

def ingest_data():
    print("--- STARTING INGESTION ---")
    
    # 2. Load the Documents
    # We are loading the two files you just created
    loader_policy = TextLoader("./data/policy.txt")
    loader_faq = TextLoader("./data/faq.txt")
    
    documents_policy = loader_policy.load()
    documents_faq = loader_faq.load()
    
    # Combine them
    all_documents = documents_policy + documents_faq
    print(f"Loaded {len(all_documents)} text files.")

    # 3. Split Text into Chunks
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(all_documents)
    print(f"Split into {len(texts)} chunks.")

    # 4. Create Vector Store (Database)
    # Using FakeEmbeddings to bypass Azure keys for now
    embeddings = FakeEmbeddings(size=1536) 
    db = FAISS.from_documents(texts, embeddings)
    
    # 5. Save locally
    db.save_local("vector_store")
    print("--- SUCCESS: Database saved to 'vector_store/' folder ---")

if __name__ == "__main__":
    ingest_data()