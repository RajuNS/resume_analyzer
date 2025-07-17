// static/js/main.js
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('analyzer-form');
    const resumeInput = document.getElementById('resume');
    const fileNameSpan = document.getElementById('file-name');

    // Update file name in custom input
    resumeInput.addEventListener('change', () => {
        if (resumeInput.files.length > 0) {
            fileNameSpan.textContent = resumeInput.files[0].name;
        } else {
            fileNameSpan.textContent = 'Click to select a file...';
        }
    });

    form.addEventListener('submit', async function (e) {
        e.preventDefault();

        const formData = new FormData(form);
        
        const loader = document.getElementById('loader');
        const resultsDiv = document.getElementById('results');
        const errorDiv = document.getElementById('error-message');
        const submitBtn = document.getElementById('submit-btn');

        // Show loader and hide previous results/errors
        loader.style.display = 'block';
        resultsDiv.style.display = 'none';
        errorDiv.style.display = 'none';
        submitBtn.disabled = true;
        submitBtn.innerHTML = `
            <div class="loader-btn"></div>
            Analyzing...
        `;

        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                body: formData,
            });

            const result = await response.json();

            if (response.ok) {
                displayResults(result);
            } else {
                displayError(result.error || 'An unknown error occurred.');
            }
        } catch (error) {
            console.error('Fetch error:', error);
            displayError('An unexpected network error occurred. Please check the console.');
        } finally {
            // Hide loader and re-enable button
            loader.style.display = 'none';
            submitBtn.disabled = false;
            submitBtn.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                Analyze Now
            `;
        }
    });
});

function displayError(message) {
    const errorDiv = document.getElementById('error-message');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
}

function displayResults(data) {
    const resultsDiv = document.getElementById('results');
    const finalScoreEl = document.getElementById('final-score');
    const scoreCircle = document.getElementById('score-circle');
    
    // Animate score circle
    scoreCircle.style.setProperty('--value', data.final_score);
    finalScoreEl.textContent = data.final_score + '%';

    document.getElementById('skill-score').textContent = data.skill_match_score + '%';
    document.getElementById('similarity-score').textContent = data.context_similarity_score + '%';

    const matchedList = document.getElementById('matched-skills');
    updateSkillList(matchedList, data.matched_skills, 'No matching skills found.');

    const missingList = document.getElementById('missing-skills');
    updateSkillList(missingList, data.missing_skills, 'All required skills are present!');

    resultsDiv.style.display = 'block';
}

function updateSkillList(listElement, skills, emptyMessage) {
    listElement.innerHTML = ''; // Clear previous results
    if (skills.length > 0) {
        skills.forEach(skill => {
            const li = document.createElement('li');
            li.textContent = skill;
            listElement.appendChild(li);
        });
    } else {
        const li = document.createElement('li');
        li.textContent = emptyMessage;
        li.style.background = 'none';
        li.style.color = 'var(--subtle-text)';
        listElement.appendChild(li);
    }
}