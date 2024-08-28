# test_chromadb.py

from chromadb import Client

def test_chromadb():
    # Step 1: Initialize ChromaDB Client
    client = Client()
    print("ChromaDB client initialized.")

    # Step 2: Create a Collection
    collection = client.create_collection(name="test_collection")
    print("Collection 'test_collection' created.")

    # Step 3: Insert Data
    documents = [
        {"id": "doc1", "text": "ChromaDB is a vector database.", "embedding": [0.1, 0.2, 0.3]},
        {"id": "doc2", "text": "It is used to manage embeddings.", "embedding": [0.2, 0.1, 0.4]},
    ]

    for doc in documents:
        collection.add(doc["id"], doc["embedding"])
    print(f"Inserted {len(documents)} documents into the collection.")

    # Step 4: Query the Collection
    query_vector = [0.1, 0.2, 0.3]  # Example query vector
    results = collection.query(query_vector, n_results=2)  # Get 2 nearest vectors
    print("Query results:")
    for result in results:
        print(result)

    # Step 5: Clean Up
    collection.delete("doc1")
    collection.delete("doc2")
    print("Test documents deleted.")

if __name__ == "__main__":
    test_chromadb()
