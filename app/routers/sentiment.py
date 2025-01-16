import re
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter()


class TextInput(BaseModel):
    text: str


# Load the sentiment analysis pipeline with a different model
sentiment_pipeline = pipeline(
    "sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


def preprocess_text(text: str) -> str:
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


@router.post("/predict")
async def predict_sentiment(input: TextInput):
    try:
        preprocessed_text = preprocess_text(input.text)
        result = sentiment_pipeline(preprocessed_text)
        return {"sentiment": result[0]['label'], "score": result[0]['score']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
