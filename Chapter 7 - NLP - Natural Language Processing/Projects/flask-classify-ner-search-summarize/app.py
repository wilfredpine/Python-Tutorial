# app.py

from flask import Flask, render_template, request, redirect, url_for
from utils.classifier import classify_document
from utils.ner import extract_entities
from utils.summarizer import summarize_text
from utils.search import search_documents
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
#app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['document']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            with open(filepath, 'r') as f:
                content = f.read()
                
            classification = classify_document(content)
            entities = extract_entities(content)
            summary = summarize_text(content)
            
            return render_template('results.html', classification=classification, entities=entities, summary=summary)
    
    return render_template('upload.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        results = search_documents(query)
        return render_template('results.html', search_results=results)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
