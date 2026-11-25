from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_analyze_valid_text():
    response = client.post(
        "/analyze",
        json={"text": "  The cat sat.\n\nThe dog ran!  Did the cat see?  "},
    )
    assert response.status_code == 200
    assert response.json() == {
        "word_count": 10,
        "character_count": 42,
        "sentence_count": 3,
        "unique_word_count": 7,
        "top_words": [["the", 3], ["cat", 2], ["did", 1], ["dog", 1], ["ran", 1]],
    }


def test_analyze_empty_text_returns_422():
    response = client.post("/analyze", json={"text": ""})
    assert response.status_code == 422


def test_analyze_whitespace_only_text_returns_422():
    response = client.post("/analyze", json={"text": "   \n\t "})
    assert response.status_code == 422


def test_analyze_missing_text_field_returns_422():
    response = client.post("/analyze", json={})
    assert response.status_code == 422
