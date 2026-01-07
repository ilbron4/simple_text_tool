from app.logger import log_info, log_error
from app.config import DATA_DIR, OUTPUT_DIR
from utils.reader import read_file
from utils.processor import count_text

class TextAnalyzer:
    def run(self, filename):
        file_path = DATA_DIR / filename

        if not file_path.exists():
            log_error("Filen finns inte")
            return

        text = read_file(file_path)
        lines, words = count_text(text)

        log_info(f"Antal rader: {lines}")
        log_info(f"Antal ord: {words}")

        OUTPUT_DIR.mkdir(exist_ok=True)
        with open(OUTPUT_DIR / "result.txt", "w", encoding="utf-8") as f:
            f.write(f"Antal rader: {lines}\n")
            f.write(f"Antal ord: {words}\n")
