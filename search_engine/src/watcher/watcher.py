"""
File watcher module for automatic index rebuilding.

This module monitors the corpus directory for any changes to `.txt` files.
When a change is detected (create, modify, delete), it automatically rebuilds
the inverted index and persists it to disk using pickle.

Dependencies:
    - watchdog
    - nltk
    - pickle
"""

import os
import pickle
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.indexing import load_documents, build_inverted_index
from src.preprocessing.text_cleaner import preprocess
from src.config import dataDir, indexFile

def build_index():
    """
    Loads all documents, preprocesses them, builds an inverted index,
    and saves both the index and document lengths to disk as a .pkl file.
    """

    print("[Watcher] Rebuilding index...")
    docs = load_documents(dataDir)
    index, doc_lengths = build_inverted_index(docs, preprocess)

    if not os.path.exists("index"):
        os.makedirs("index")

    with open(indexFile, "wb") as f:
        pickle.dump((index, doc_lengths), f)

    print("[Watcher] Index updated")

class CorpusChangeHandler(FileSystemEventHandler):
    """
    Event handler for detecting changes in the corpus directory.

    Triggers a rebuild of the inverted index when any `.txt` file is
    created, modified, or deleted.
    """

    def on_any_event(self, event):
        if event.src_path.endswith(".txt"):
            build_index()

def run_watcher():
    """
    Starts a file system watcher on the corpus directory.

    On detecting any change to `.txt` files (recursively), the
    inverted index is rebuilt. The function runs indefinitely until
    interrupted (e.g., via Ctrl+C).
    """
        
    print(f"[Watcher] Starting watcher at {dataDir}/ directory")
    build_index() # Build index at startup

    event_handler = CorpusChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=dataDir, recursive=True)
    observer.start()

    try:
        while True:
            pass  # El process remains running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
