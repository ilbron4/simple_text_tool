def count_text(text):
    lines = text.splitlines()
    words = text.split()
    return len(lines), len(words)
