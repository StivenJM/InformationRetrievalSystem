# bin/index_service.py
"""
Starts the file watcher to monitor the corpus and rebuild the inverted index
whenever changes occur.
"""

from src.watcher import run_watcher

if __name__ == "__main__":
    run_watcher()
