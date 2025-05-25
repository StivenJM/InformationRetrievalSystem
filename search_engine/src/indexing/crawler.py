# Load documents

import os
from typing import Dict

def load_documents(directory: str) -> Dict[str, str]:
    """
    Loads all .txt files from a specified directory and returns their content.

    This function scans the given directory, reads the contents of each file 
    with a `.txt` extension, and stores the content in a dictionary. The keys 
    are the filenames, and the values are the full text content of the files.

    Args:
        directory (str): Relative path to app's directory containing .txt files.

    Returns:
        Dict[str, str]: A dictionary where each key is the absolute file path to a .txt file,
        and the corresponding value is the file's content as a UTF-8 string.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        UnicodeDecodeError: If a file cannot be decoded using UTF-8.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")
    
    documents = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                full_path = os.path.abspath(os.path.join(root, file))
                with open(full_path, "r", encoding="utf-8") as f:
                    documents[full_path] = f.read()

    return documents
