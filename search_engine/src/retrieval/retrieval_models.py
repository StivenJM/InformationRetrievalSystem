# Implements BM25

import math
from typing import Dict, List, Tuple
from collections import defaultdict

def bm25_score(
    query_terms: List[str],
    index: Dict[str, List[Tuple[str, int]]],
    doc_lengths: Dict[str, int],
    k1: float = 1.5,
    b: float = 0.75
) -> Dict[str, float]:
    """
    Computes BM25 scores (relevance) for documents that contain query terms.

    Args:
        query_terms (List[str]): Tokenized query terms.
        index (Dict[str, List[Tuple[str, int]]]): Inverted index.
        doc_lengths (Dict[str, int]): Total tokens per document.
        k1 (float): BM25 tuning parameter.
        b (float): BM25 tuning parameter.

    Returns:
        (Dict[str, float]): Mapping of doc_id to BM25 score.
    """
    
    scores: Dict[str, float] = defaultdict(float)
    N = len(doc_lengths) # Corpus' size
    avgdl = sum(doc_lengths.values()) / N # Average document size

    for term in query_terms:
        if term not in index:
            continue
        postings = index[term]
        df = len(postings)
        idf = math.log(1 + (N - df + 0.5) / (df + 0.5))

        for doc_id, tf in postings:
            dl = doc_lengths[doc_id]
            score = idf * (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * dl / avgdl))
            scores[doc_id] += score

    return dict(scores)
