# bin/search_client_test.py

import socket
import json

HOST = "127.0.0.1"
PORT = 9000

query = input("Ingresa tu búsqueda: ").strip()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(query.encode("utf-8"))

    data = s.recv(4096).decode("utf-8")
    results = json.loads(data)

    print("\n[Resultados]")
    for doc_id, score in results:
        print(f"{doc_id} | Score: {score:.4f}")
