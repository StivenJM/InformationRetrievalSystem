import os
import subprocess
import sys

REQUIREMENTS = [
    "nltk>=3.8.1",
    "python-dotenv>=1.0.0",
    "watchdog>=3.0.0",
    "pytest>=7.0.0"
]

def write_requirements():
    with open("requirements.txt", "w") as f:
        for dep in REQUIREMENTS:
            f.write(dep + "\n")
    print("[✓] requirements.txt created.")

def create_venv():
    if not os.path.isdir(".venv"):
        print("[…] Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", ".venv"])
        print("[✓] .venv created.")
    else:
        print("[✓] .venv already exists.")

if __name__ == "__main__":
    print(" Setting up project...")
    write_requirements()
    create_venv()
    print("\n Project is ready! To activate your environment:\n")

    print("Now run the following command to activate your environment:")
    print("  .venv\\Scripts\\activate" if os.name == "nt" else "  source .venv/bin/activate")
    print("Then run:")
    print("  pip install -r requirements.txt")
