# KSIT Virtual Assistant

An intelligent, conversational FAQ chatbot for K. S. Institute of Technology, built with Python, Flask, and advanced NLP techniques.

## Features

-   **Natural Language Understanding:** Powered by TF-IDF and Cosine Similarity, the bot understands the user's intent rather than just matching keywords.
-   **Dynamic & Responsive UI:** The interface provides a smooth user experience with a welcome message, typing indicators, and suggested questions.
-   **Expandable Knowledge Base:** Uses a structured `faq.json` file that is easy to update and scale with new information.

## Technical Implementation

### Backend (NLP Engine)

The chatbot's core logic was upgraded from a simple keyword search to a more sophisticated NLP pipeline:

-   **TF-IDF & Cosine Similarity:** The bot uses a Term Frequency-Inverse Document Frequency (TF-IDF) vectorizer to analyze user questions and find the most contextually relevant answer from the knowledge base. This allows it to understand queries even if they don't use the exact keywords.
-   **Lemmatization:** User input is preprocessed using NLTK's `WordNetLemmatizer` to reduce words to their base form (e.g., "studies" becomes "study"). This makes the matching process more robust and accurate.
-   **Structured JSON Knowledge Base:** The original `faq.txt` was replaced with a `faq.json` file. This provides a more structured and scalable way to manage the question tags and answers.

### Frontend (User Experience)

The user interface was enhanced to feel more modern and interactive:

-   **Initial Welcome Message:** The bot now greets the user as soon as the page loads.
-   **Typing Indicator:** A "typing..." animation provides visual feedback to the user while the bot is processing a request.
-   **Suggested Questions:** Buttons with common queries help guide the user and showcase the bot's capabilities.

## How to Run Locally

1.  **Clone the repository:**
    ```
    git clone https://github.com/your-username/ksit-chatbot.git
    cd ksit-chatbot
    ```

2.  **Create and activate a virtual environment:**
    ```
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```
    pip install Flask nltk scikit-learn
    ```

4.  **Run the application:**
    ```
    python app.py
    ```
    Open your browser and navigate to `http://127.0.0.1:5000`.

## Folder Structure

```
ksit-chatbot/
├── app.py          # Main Flask application with NLP logic
├── faq.json        # Structured knowledge base for the chatbot
├── README.md       # Project documentation
├── .gitignore      # Specifies files for Git to ignore
├── static/
│   └── ksit_logo.jpg
└── templates/
    └── index.html
```
```

### 2. Push the Documentation Update to GitHub

Now that you have the new content, follow the same Git workflow you've been practicing ([3][4]) to get it onto your GitHub profile.

1.  **Stage the Change:**
    In your PowerShell terminal, add the updated `README.md` file to the staging area.
    ```powershell
    git add README.md
    ```

2.  **Commit the Change:**
    Commit the file with a clear, professional message.
    ```powershell
    git commit -m "docs: Update README with new features and technical details"
    ```

3.  **Push to GitHub:**
    Send your new commit to your remote repository.
    ```powershell
    git push
    ```

Your GitHub repository is now fully up-to-date, with professional documentation that accurately reflects the advanced state of your project.
