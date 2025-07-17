from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.metrics.pairwise import cosine_similarity # type: ignore
from feature_extractor import preprocess_text # <-- This line is corrected

def calculate_skill_score(resume_skills, jd_skills):
    """
    Calculates the skill match score based on common skills.
    Score = (Number of Matched Skills / Total Skills in JD)
    """
    if not jd_skills:
        return 0.0

    # Ensure skills are compared in a case-insensitive manner
    resume_skills_lower = {skill.lower() for skill in resume_skills}
    jd_skills_lower = {skill.lower() for skill in jd_skills}

    matched_skills = resume_skills_lower.intersection(jd_skills_lower)
    
    score = len(matched_skills) / len(jd_skills_lower) if len(jd_skills_lower) > 0 else 0.0
    return score

def calculate_similarity_score(resume_text, jd_text):
    """
    Calculates the cosine similarity between resume and JD text.
    """
    # Preprocess the texts
    processed_resume = preprocess_text(resume_text)
    processed_jd = preprocess_text(jd_text)
    
    if not processed_resume or not processed_jd:
        return 0.0
    
    texts = [processed_resume, processed_jd]
    
    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer()
    try:
        tfidf_matrix = vectorizer.fit_transform(texts)
    except ValueError:
        # Happens if one of the documents is empty after preprocessing
        return 0.0
    
    # Calculate cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    return similarity[0][0]
