# app.py (Corrected to fix NLTK version issues)

from flask import Flask, render_template, request, jsonify
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# --- FIX: A simpler and more robust way to ensure NLTK packages are present ---
# This will download the packages only if they are missing.
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

app = Flask(__name__)

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Preprocessing function that includes lemmatization
def preprocess(text):
    tokens = word_tokenize(text.lower())
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(lemmas)

# Load FAQs and preprocess them
def load_faqs(file_path):
    try:
        with open(file_path, 'r') as file:
            faq_data = json.load(file)
        # Preprocess each document's tags
        documents = [preprocess(" ".join(item['tags'])) for item in faq_data['questions']]
        answers = [item['answer'] for item in faq_data['questions']]
        return documents, answers
    except FileNotFoundError:
        print(f"Error: FAQ file not found at {file_path}")
        return [], []
    except Exception as e:
        print(f"Error loading FAQ file: {e}")
        return [], []

# Load the FAQs and prepare the TF-IDF model
faq_documents, faq_answers = load_faqs('faq.json')
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(faq_documents)

# The smarter function to find an answer
def find_answer_tfidf(user_question):
    if not faq_documents:
        return "Sorry, my knowledge base is currently unavailable."
        
    # Preprocess the user's question
    processed_question = preprocess(user_question)
    
    user_question_vector = vectorizer.transform([processed_question])
    cosine_similarities = cosine_similarity(user_question_vector, tfidf_matrix).flatten()
    best_match_index = np.argmax(cosine_similarities)
    
    if cosine_similarities[best_match_index] > 0.1:
        return faq_answers[best_match_index]
    else:
        return "Sorry, I couldn't find a relevant answer. Could you please rephrase?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def get_bot_response():
    user_message = request.args.get('msg')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    response = find_answer_tfidf(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
