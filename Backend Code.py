from flask import Flask, request, render_template
import fitz  # PyMuPDF
import spacy
import re
import os

app = Flask(_name_)
nlp = spacy.load("en_core_web_sm")

def extract_text(file):
    text = ""
    if file.filename.endswith('.pdf'):
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
    return text

def parse_cv(text):
    doc = nlp(text)
    email = re.findall(r'\S+@\S+', text)
    phone = re.findall(r'\+?\d[\d\s()-]{8,}\d', text)
    skills = ['Python', 'Java', 'SQL', 'Machine Learning']
    found_skills = [skill for skill in skills if skill.lower() in text.lower()]
    return {
        'name': doc.ents[0].text if doc.ents else 'N/A',
        'email': email[0] if email else 'N/A',
        'phone': phone[0] if phone else 'N/A',
        'skills': found_skills
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['resume']
    text = extract_text(file)
    parsed_data = parse_cv(text)
    return render_template('result.html', data=parsed_data)

if _name_ == '_main_':
    app.run(debug=True)