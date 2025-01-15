from fastapi import APIRouter, HTTPException
from app.models.sentiment_model import SentimentModel

router = APIRouter()
model = SentimentModel()

@router.post("/predict")
async def predict_sentiment(text: str):
    if not text:
        raise HTTPException(status_code=400, detail="Text input is required")
    sentiment = model.predict_sentiment(text)
    return {"sentiment": sentiment}