import json
from pathlib import Path

# Projektets rotmapp
ROOT = Path(__file__).resolve().parents[2]

# Läs config.json
with open(ROOT / "config.json", "r", encoding="utf-8") as f:
    CONFIG = json.load(f)

# Exponerade sökvägar
DATA_DIR = ROOT / CONFIG["data_dir"]
OUTPUT_DIR = ROOT / CONFIG["output_dir"]
