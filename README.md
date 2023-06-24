```markdown
# Sentiment Analysis API

This project implements a web API for performing sentiment analysis on text using a pre-trained machine learning model. It provides a single endpoint to analyze the sentiment of text input and returns the sentiment analysis result as a JSON response.

## Requirements

- Python 3.7+
- Django 3.2 or higher
- transformers library
- Other project dependencies (listed in requirements.txt)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Shahid-Fahad/Sentiment-Analysis-API.git
   ```

2. Navigate to the project directory:

   ```shell
   cd Sentiment-Analysis-API
   ```

3. (Optional) Create and activate a virtual environment:

   ```shell
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate  # For Windows
   ```

4. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

5. Run the development server:

   ```shell
   python manage.py runserver
   ```

6. The API will be accessible at http://localhost:8000/analyze.

## API Endpoint

### Analyze Sentiment

- **URL**: `/analyze`
- **Method**: POST
- **Request Payload**: JSON object with the following structure:

   ```json
   {
     "text": "Text to be analyzed"
   }
   ```

- **Response**: JSON object with the following structure:

   ```json
   {
     "sentiment": "positive/negative/neutral"
   }
   ```
