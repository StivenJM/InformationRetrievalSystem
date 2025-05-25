import socket
import json

class TcpClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def query(self, query: str):
        """
        Sends a query to server and returns a json
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(query.encode("utf-8"))
            data = s.recv(8192).decode("utf-8")

        raw_results = json.loads(data)
        return raw_results