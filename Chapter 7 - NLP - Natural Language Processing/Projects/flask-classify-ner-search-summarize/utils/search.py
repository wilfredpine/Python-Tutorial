# utils/search.py

import os

def search_documents(query):
    results = []
    for filename in os.listdir('uploads/'):
        if filename.endswith('.txt'):
            with open(os.path.join('uploads/', filename), 'r') as file:
                content = file.read()
                if query.lower() in content.lower():
                    results.append(filename)
    return results
