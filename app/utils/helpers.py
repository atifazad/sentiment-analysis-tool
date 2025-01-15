def preprocess_text(text: str) -> str:
    # Basic text preprocessing steps
    text = text.strip()  # Remove leading and trailing whitespace
    text = text.lower()  # Convert to lowercase
    return text

def format_response(prediction: dict) -> dict:
    # Format the response from the model for the API
    return {
        "label": prediction.get("label"),
        "score": prediction.get("score")
    }