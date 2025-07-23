NLP-Powered Resume Analyzer
An intelligent web application built with Python and Flask that analyzes resumes against job descriptions, providing a data-driven match score and a detailed breakdown of missing skills.

(Note: You should replace the link above with a URL to a real screenshot of your project.)

Key Features
Dual-Scoring System: Calculates a comprehensive match score by combining:

Keyword Matching: Identifies direct skill overlap.

Semantic Similarity: Uses TF-IDF and Cosine Similarity to understand the contextual relevance of the resume, even if the exact keywords don't match.

Detailed Skill Analysis: Clearly displays which skills from the job description were found in the resume and which are missing.

Multi-Format Support: Parses both .pdf and .docx resume files to extract text content.

Responsive UI: A clean and intuitive user interface built with HTML, CSS, and JavaScript that provides a seamless experience on any device.

Tech Stack
Backend: Python, Flask

NLP & Machine Learning: Scikit-learn, spaCy, NLTK

File Parsing: PyMuPDF, python-docx

Frontend: HTML5, CSS3, JavaScript

How It Works
Upload & Paste: The user uploads their resume and pastes the text of a job description into the web form.

Text Extraction: The Flask backend uses PyMuPDF or python-docx to parse the uploaded file and extract the raw text.

NLP Preprocessing: Both the resume and job description text are cleaned, tokenized, and lemmatized using NLP libraries to prepare them for analysis.

Scoring Algorithm: The processed texts are converted into numerical vectors using TF-IDF. The Cosine Similarity between these vectors is then calculated to determine the semantic match score. This is combined with a direct keyword match score.

Display Results: The final weighted score and the lists of matched/missing skills are sent back to the frontend and dynamically displayed to the user.

Getting Started
To get a local copy up and running, follow these simple steps.

Prerequisites
Python 3.8+

pip

Installation
Clone the repository:

git clone https://github.com/your-username/resume_analyzer.git
cd resume_analyzer

Create and activate a virtual environment:

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

Download the spaCy language model:

python -m spacy download en_core_web_sm

Run the Flask application:

python app.py

Open your browser and navigate to http://127.0.0.1:5000 to use the application.
