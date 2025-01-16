import re
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter()


class TextInput(BaseModel):
    text: str


# Load the emotion classification pipeline with the new model
emotion_pipeline = pipeline(
    "text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)


@router.post("/predict")
async def predict_emotion(input: TextInput):
    try:
        result = emotion_pipeline(input.text)
        # Extract the highest scoring emotion
        highest_emotion = max(result[0], key=lambda x: x['score'])
        return {"emotion": highest_emotion['label'], "score": highest_emotion['score']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
