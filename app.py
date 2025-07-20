# app.py (Updated)

import os
from flask import Flask, render_template, request, jsonify
import nltk
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# Load FAQs from a file into a dictionary for easy lookup
def load_faqs(file_path):
    faqs = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Each line is in the format 'Keyword, Content'
                parts = line.strip().split(',', 1)  # Split on the first comma only
                if len(parts) == 2:
                    keyword, content = parts
                    # FIX: Strip quotes from the keyword and convert to lower case for better matching
                    faqs[keyword.strip('"').lower()] = content.strip().strip('"')
    except FileNotFoundError:
        print(f"Error: FAQ file not found at {file_path}")
    except Exception as e:
        print(f"Error loading FAQ file: {str(e)}")
    
    return faqs

# Preprocess the input question
def process_question(question):
    tokens = word_tokenize(question.lower())  # Tokenizing and converting to lowercase
    return tokens

# Find the most relevant answer from the FAQs
def find_answer(user_question, faqs):
    processed_question = process_question(user_question)
    best_match = None
    best_match_score = 0
    
    # Loop through the FAQ dictionary
    for keyword, content in faqs.items():
        # Check if any part of the user's question matches the keyword
        if keyword in user_question.lower():
            return content # Return immediately on a simple substring match for better results

    # If no substring match, fall back to token-based matching
    for keyword, content in faqs.items():
        tokens = word_tokenize(keyword)
        common_tokens = set(processed_question).intersection(tokens)
        score = len(common_tokens)
        
        if score > best_match_score:
            best_match_score = score
            best_match = content
    
    if best_match:
        return best_match
    else:
        return "Sorry, I couldn't find an answer for that. Could you please rephrase your question?"

# Load the FAQs once when the app starts
faq_file_path = "faq.txt"  # Ensure the correct path to your faq.txt
faqs = load_faqs(faq_file_path)

@app.route('/')
def index():
    return render_template('index.html')

# FIX: Changed route and method to match the frontend JavaScript request
@app.route('/get', methods=['GET'])
def get_bot_response():
    # FIX: Get the message from URL query parameters (e.g., /get?msg=hello)
    user_message = request.args.get('msg')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    response = find_answer(user_message, faqs)
    return jsonify({'response': response})

if __name__ == '__main__':
    # You only need to download this once. Can be commented out after first run.
    try:
        nltk.data.find('tokenizers/punkt')
    except nltk.downloader.DownloadError:
        nltk.download('punkt')
        
    app.run(debug=True)  # Run the app in debug mode
