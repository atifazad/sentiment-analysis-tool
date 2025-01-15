from fastapi import FastAPI
from app.routers import sentiment

app = FastAPI()

app.include_router(sentiment.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis Tool!"}