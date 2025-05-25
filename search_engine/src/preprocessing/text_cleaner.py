"""
Text preprocessing module.

This module provides basic preprocessing functionality including tokenization,
lowercasing, stopword removal, and filtering of non-alphabetic tokens.
It is designed to clean text before building an inverted index.

Dependencies:
    - nltk (Natural Language Toolkit)

Before using this module, ensure that NLTK resources are downloaded:
    - punkt (for tokenization)
    - stopwords (for filtering common words)
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from typing import List

# Download required NLTK resources (only if not already present)
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

# Load Spanish stopwords
stop_words = set(stopwords.words("spanish"))

def preprocess(text: str) -> List[str]:
    """
    Preprocesses input text by tokenizing, converting to lowercase,
    removing non-alphabetic tokens, and filtering out stopwords.

    Args:
        text (str): Raw input text to be cleaned.

    Returns:
        List[str]: A list of processed tokens.
    """
    tokens = word_tokenize(text.lower())
    return [
        word for word in tokens
        if word.isalpha() and word not in stop_words
    ]
