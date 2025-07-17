# feature_extractor.py
import spacy
from spacy.matcher import PhraseMatcher

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# --- IMPORTANT: Build a comprehensive skill list ---
# This is a sample list. For a real application, this list should be
# much larger and could be loaded from a file (e.g., CSV, JSON).
SKILL_LIST = [
    'python', 'java', 'c++', 'javascript', 'sql', 'html', 'css',
    'react', 'angular', 'vue', 'node.js', 'django', 'flask',
    'machine learning', 'data science', 'artificial intelligence',
    'natural language processing', 'nlp', 'computer vision',
    'pandas', 'numpy', 'scikit-learn', 'tensorflow', 'pytorch',
    'aws', 'azure', 'google cloud', 'gcp', 'docker', 'kubernetes',
    'git', 'jira', 'agile', 'scrum', 'data analysis', 'project management'
]

def preprocess_text(text):
    """
    Preprocesses text: lowercasing, tokenization, lemmatization,
    and removal of stopwords and punctuation.
    """
    doc = nlp(text.lower())
    processed_tokens = [
        token.lemma_ for token in doc
        if not token.is_stop and not token.is_punct and token.is_alpha
    ]
    return " ".join(processed_tokens)

def extract_skills(text):
    """
    Extracts skills from text using spaCy's PhraseMatcher.
    """
    matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
    skill_patterns = [nlp.make_doc(skill) for skill in SKILL_LIST]
    matcher.add('Skills', skill_patterns)

    doc = nlp(text)
    matches = matcher(doc)
    
    found_skills = set()
    for _, start, end in matches:
        span = doc[start:end]
        found_skills.add(span.text.lower())
        
    return list(found_skills)