from src.data_loader import load_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

# Example usage

if __name__ == "__main__":
    # data_path = "data"
    # documents = load_documents(data_path)
    store = FaissVectorStore(persist_dir="faiss_store")
    # store.build_from_documents(documents)
    store.load()  # Load existing index if available
    # print(store.query("What is Quantum Computing?", top_k=3))  # Example query

    rag_search = RAGSearch()
    query = "What are the Best Practices & Tactical Recommendations of quantum computing?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)