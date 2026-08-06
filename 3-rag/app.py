from src.data_loader import load_documents
from src.embedding import EmbeddingPipeline

# Example usage

if __name__ == "__main__":
    data_path = "data"  # Replace with your actual data path
    documents = load_documents(data_path)
    chunks = EmbeddingPipeline().chunk_documents(documents)
    vectors = EmbeddingPipeline().embed_chunks(chunks)

    print(f"[INFO] Total documents loaded: {len(documents)}")