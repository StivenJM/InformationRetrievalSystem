# bin/search_service.py
"""
Search service module.
This script runs a local TCP server that listens for search queries from the GUI
and responds with ranked search results using the BM25 model.
"""

import pickle
import socket
import json
from src.preprocessing.query_processor import process_query
from src.retrieval import bm25_score, rank_documents
from src.config import indexFile, ipHost, port

def load_index():
    with open(indexFile, "rb") as f:
        return pickle.load(f)

def handle_query(query: str, index, doc_lengths):
    terms = process_query(query)
    scores = bm25_score(terms, index, doc_lengths)
    ranked = rank_documents(scores)
    return ranked

def search_service(host: str = ipHost, port: int = port):
    index, doc_lengths = load_index()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen()
        print(f"[SearchService] Listening on {host}:{port}...")

        try:
            while True:
                conn, addr = server.accept()

                with conn:
                    data = conn.recv(1024).decode("utf-8")
                    if not data:
                        continue
                    print(f"[SearchService] Received query: {data}")
                    results = handle_query(data, index, doc_lengths)
                    response = json.dumps(results)
                    conn.sendall(response.encode("utf-8"))
        except KeyboardInterrupt:
            print("[SearchService] Shutting down.")
        except Exception:
            print("Unexpected error")

if __name__ == "__main__":
    search_service()
