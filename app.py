# app.py
from flask import Flask, render_template, request, jsonify # type: ignore
import os
import uuid

# Import your custom modules
from parser import extract_text
from feature_extractor import extract_skills
from scorer import calculate_skill_score, calculate_similarity_score

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files or 'jd' not in request.form:
        return jsonify({'error': 'Missing resume file or job description'}), 400

    resume_file = request.files['resume']
    jd_text = request.form['jd']
    
    if resume_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Securely save the uploaded file with a unique name
    filename = f"{uuid.uuid4().hex}_{resume_file.filename}"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    try:
        resume_file.save(file_path)

        # 1. Parsing & Extraction
        resume_text = extract_text(file_path)
        
        # 2. Feature Extraction
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text)

        # 3. Scoring
        skill_score = calculate_skill_score(resume_skills, jd_skills)
        similarity_score = calculate_similarity_score(resume_text, jd_text)
        
        # 4. Final Weighted Score
        # Weights can be adjusted based on importance
        final_score = (0.6 * skill_score) + (0.4 * similarity_score)
        
        # Prepare results
        matched_skills = list(set(resume_skills) & set(jd_skills))
        missing_skills = list(set(jd_skills) - set(resume_skills))
        
        result = {
            'final_score': round(final_score * 100, 2),
            'skill_match_score': round(skill_score * 100, 2),
            'context_similarity_score': round(similarity_score * 100, 2),
            'matched_skills': matched_skills,
            'missing_skills': missing_skills
        }
        
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500
    finally:
        # Clean up the uploaded file
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == '__main__':
    app.run(debug=True)