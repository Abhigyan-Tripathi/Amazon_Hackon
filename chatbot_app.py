from flask import Flask, request, jsonify
import nltk
from nltk.corpus import stopwords
from transformers import pipeline

# Set up the Flask application
app = Flask(__name__)

# Disable SSL certificate verification for NLTK
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download NLTK stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Function to preprocess text
def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word.lower() not in stop_words]
    return ' '.join(tokens)

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline('sentiment-analysis')

# Function to handle query
def handle_query(query):
    processed_text = preprocess_text(query)
    sentiment_result = sentiment_pipeline(processed_text)[0]
    response = "Your query has been processed."
    sentiment = sentiment_result['label']
    return response, sentiment

# Define the /query endpoint
@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    query = data.get('query', '')
    response, sentiment = handle_query(query)
    return jsonify({'response': response, 'sentiment': sentiment})

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5001)
