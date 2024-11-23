# utils/summarizer.py

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']
