from src.data_loader import load_documents
from src.vectorstore import FaissVectorStore

# Example usage

if __name__ == "__main__":
    data_path = "data"  # Replace with your actual data path
    # documents = load_documents(data_path)
    store = FaissVectorStore(persist_dir="faiss_store", embedding_model="all-MiniLM-L6-v2")
    # store.build_from_documents(documents)
    store.load()  # Load existing index if available

    print(store.query("What is Quantum Computing?", top_k=3))  # Example query