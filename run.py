import sys
from pathlib import Path

# Lägg till src i Python path
sys.path.append(str(Path(__file__).parent / "src"))

from app.main import TextAnalyzer

if __name__ == "__main__":
    analyzer = TextAnalyzer()
    analyzer.run("example.txt")
