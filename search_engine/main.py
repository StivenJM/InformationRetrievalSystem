# main.py
"""
Main launcher script for the Retrieval Information System.
This script starts all core services: indexing, search, and GUI.
"""
import subprocess
import sys
import os

def start_service(script_name: str):
    """
    Launch a Python script from the bin/ directory as a subprocess.
    """
    bin_path = os.path.join(os.path.dirname(__file__), "bin")
    return subprocess.Popen([sys.executable, os.path.join(bin_path, script_name)])

def main():
    print("[Main] Starting all system services...")

    index_proc = start_service("index_service.py")
    search_proc = start_service("search_service.py")
    gui_proc = start_service("gui_service.py")

    print("[Main] All services launched. Press Ctrl+C to stop.")

    try:
        index_proc.wait()
        search_proc.wait()
        gui_proc.wait()
    except KeyboardInterrupt:
        print("\n[Main] Terminating services...")
        index_proc.terminate()
        search_proc.terminate()
        gui_proc.terminate()
        index_proc.wait()
        search_proc.wait()
        gui_proc.wait()
        print("[Main] Shutdown complete.")

if __name__ == "__main__":
    main()
