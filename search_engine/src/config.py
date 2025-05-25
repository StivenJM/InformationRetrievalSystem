import os
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

# Directory path where the corpus data (text documents) is stored.
# Expected to be defined in the .env file as: DATA_DIR=path/to/data
dataDir = os.getenv("DATA_DIR")

# Directory path where the inverted index will be saved or loaded from.
# Expected to be defined in the .env file as: INDEX_DIR=path/to/index
indexDir = os.getenv("INDEX_DIR")

# The filename used to store the serialized inverted index.
# Expected to be defined in the .env file as: INDEX_FILE_NAME=inverted_index.pkl
indexFileName = os.getenv("INDEX_FILE_NAME")

# Full file path to the inverted index file, combining directory and filename.
indexFile = os.path.join(indexDir, indexFileName)


# ------------------------------
# Local IP Host to serve the search service to GUI
ipHost = os.getenv("IP_HOST", "127.0.0.1")

# Port to search service
port = int(os.getenv("PORT", 9000))