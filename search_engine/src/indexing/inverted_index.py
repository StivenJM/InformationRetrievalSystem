"""
Inverted index: building and management module.

This module provides functionality to construct an inverted index from
a collection of documents. It also computes the length of each document
for use in scoring models like BM25.
"""

from collections import defaultdict
from typing import Callable, Dict, List, Tuple

def build_inverted_index(
    documents: Dict[str, str],
    tokenizer: Callable[[str], List[str]]
) -> Tuple[Dict[str, List[Tuple[str, int]]], Dict[str, int]]:
    """
    Builds an inverted index from a dictionary of documents like {'doc_id': 'content'}.

    The inverted index maps each token to a list of (doc_id, frequency) pairs.
    It also calculates the total number of tokens in each document.

    Args:
        documents (Dict[str, str]): A dictionary mapping document IDs (usually file paths)
            to their raw text content.
        tokenizer (Callable[[str], List[str]]): A function that takes a string and returns
            a list of cleaned, tokenized terms.

    Returns:
        Result Tuple[Dict[str, List[Tuple[str, int]]],Dict[str, int]]:
        A tuple containing:
            - The inverted index as a dictionary mapping terms to lists of (doc_id, frequency) pairs.
            - A dictionary mapping doc_id to the total number of tokens (document length).
    """

    inverted_index: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
    doc_lengths: Dict[str, int] = {}
    
    for doc_id, text in documents.items():
        tokens = tokenizer(text)
        doc_lengths[doc_id] = len(tokens)
        freq: Dict[str, int] = defaultdict(int)
        for token in tokens:
            freq[token] += 1
        for token, count in freq.items():
            inverted_index[token].append((doc_id, count))
    
    return inverted_index, doc_lengths
