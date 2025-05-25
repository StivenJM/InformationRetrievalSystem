"""
Controller for the GUI application.
Handles interaction between the user interface and the search service.
"""

from models.Search import SearchResult
from config import HOST, PORT
from network.TcpClient import TcpClient

class SearchController:
    def __init__(self, host: str = HOST, port: int = PORT):
        self.host = host
        self.port = port

    def send_query(self, query: str) -> list[SearchResult]:
        """
        Sends a query string to the search service and returns parsed search results.

        Args:
            query (str): The user's search query.

        Returns:
            (list[SearchResult]): A list of search results from the service.
        """
        raw_results = TcpClient(HOST, PORT).query(query)
        return [SearchResult(doc_id=doc, score=score) for doc, score in raw_results]
