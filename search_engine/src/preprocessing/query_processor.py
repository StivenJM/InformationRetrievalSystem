# Preprocess user's query

from .text_cleaner import preprocess

def process_query(query: str) -> list[str]:
    """
    Applies the same preprocessing as used for documents indexing to the user query.

    Args:
        query (str): The raw user input string.

    Returns:
        list[str]: A list of cleaned, tokenized terms.
    """
    return preprocess(query)