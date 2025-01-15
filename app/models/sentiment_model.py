from transformers import pipeline

class SentimentModel:
    def __init__(self):
        self.model = pipeline("sentiment-analysis")

    def predict_sentiment(self, text: str):
        return self.model(text)