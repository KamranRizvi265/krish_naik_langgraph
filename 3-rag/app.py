from src.data_loader import load_documents


# Example usage

if __name__ == "__main__":
    data_path = "data"  # Replace with your actual data path
    documents = load_documents(data_path)
    print(f"[INFO] Total documents loaded: {len(documents)}")