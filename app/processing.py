def normalize_text(text: str) -> str:
    """
    Normalize whitespace by:
    - stripping leading/trailing whitespace
    - collapsing internal whitespace (spaces, tabs, newlines) to single spaces
    """
    return " ".join(text.split())
