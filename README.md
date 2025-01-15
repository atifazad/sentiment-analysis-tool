# Sentiment Analysis Tool

This project is a sentiment analysis tool built using FastAPI and Hugging Face Transformers. It provides a REST API for analyzing the sentiment of input text.

## Setup Instructions

1. Clone the repository:

   ```
   git clone <repository-url>
   cd sentiment-analysis-tool
   ```

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the FastAPI application, execute the following command:

```
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### API Endpoints

- **POST /sentiment**: Submit text for sentiment analysis.
  - **Request Body**:
    ```json
    {
      "text": "Your input text here"
    }
    ```
  - **Response**:
    ```json
    {
      "sentiment": "positive/negative/neutral",
      "score": 0.95
    }
    ```

## License

This project is licensed under the MIT License.
