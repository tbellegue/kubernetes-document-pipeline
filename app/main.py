from fastapi import FastAPI
from pydantic import BaseModel, field_validator

from app.processing import (
    character_count,
    normalize_text,
    sentence_count,
    top_words,
    unique_word_count,
    word_count,
)

app = FastAPI(title="Kubernetes Document Pipeline - Milestone 1")


class AnalyzeRequest(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def text_must_not_be_empty(cls, value: str) -> str:
        # Whitespace-only text would normalize to "", so treat it as empty too.
        if not value.strip():
            raise ValueError("text must not be empty")
        return value


class AnalyzeResponse(BaseModel):
    word_count: int
    character_count: int
    sentence_count: int
    unique_word_count: int
    top_words: list[tuple[str, int]]


@app.get("/")
def root():
    return {"message": "Kubernetes Document Pipeline starter is running."}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    text = normalize_text(request.text)
    return AnalyzeResponse(
        word_count=word_count(text),
        character_count=character_count(text),
        sentence_count=sentence_count(text),
        unique_word_count=unique_word_count(text),
        top_words=top_words(text),
    )
