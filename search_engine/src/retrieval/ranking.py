# Sort documents by relevance

from typing import Dict, List, Tuple

def rank_documents(scores: Dict[str, float], k: int = 10) -> List[Tuple[str, float]]:
    """
    Sorts documents by score in descending order and returns top-k.

    Args:
        scores (Dict[str, float]): Mapping of doc_id to scores (ex. BM25 score).
        k (int): Number of top results to return.

    Returns:
        (List[Tuple[str, float]]): Sorted list of (doc_id, score) pairs.
    """
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:k]