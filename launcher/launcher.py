# launcher/launcher.py

import subprocess
import sys
import os
import signal

class Launcher:
    def __init__(self):
        self.processes = []

    def start_services(self):
        python = sys.executable
        base_dir = os.path.abspath(".")
        engine_dir = os.path.join(base_dir, "search_engine")
        
        index_proc = subprocess.Popen(
            [python, "-m", "bin.index_service"],
            cwd=engine_dir
        )
        self.processes.append(index_proc)

        search_proc = subprocess.Popen(
            [python, "-m", "bin.search_service"],
            cwd=engine_dir
        )
        self.processes.append(search_proc)

        print("[Launcher] Backend services started.")

    def start_gui(self):
        python = sys.executable
        base_dir = os.path.abspath(".")

        gui_proc = subprocess.Popen(
            [python, "my_app_gui/app.py"],
            cwd=base_dir
        )
        print("[Launcher] GUI started.")
        return gui_proc

    def stop_services(self):
        print("[Launcher] Stopping backend services...")
        for proc in self.processes:
            try:
                proc.send_signal(signal.SIGINT)
                proc.wait(timeout=3)
            except Exception:
                proc.kill()
        print("[Launcher] All backend services stopped.")

def launcher():
    launcher = Launcher()
    try:
        launcher.start_services()
        gui_process = launcher.start_gui()
        gui_process.wait()  # Esperar hasta que se cierre la GUI
    except KeyboardInterrupt:
        print("[Launcher] Interrupted manually.")
    finally:
        launcher.stop_services()
        print("[Launcher] Shutdown complete.")
