from dataclasses import dataclass
from typing import List

@dataclass
class SearchResult:
    doc_id: str
    score: float

@dataclass
class SearchQuery:
    raw_query: str
    results: List[SearchResult]