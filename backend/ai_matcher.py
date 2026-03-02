class SimpleAIMatcher:
    """AI-powered job matching engine"""
    
    def __init__(self):
        self.skill_weights = {
            'python': 10, 'java': 10, 'javascript': 9,
            'react': 9, 'angular': 8, 'vue': 8,
            'django': 8, 'flask': 7, 'node': 8,
            'sql': 7, 'mongodb': 6, 'aws': 8,
            'docker': 7, 'kubernetes': 8, 'git': 6
        }
    
    def calculate_match_score(self, user_skills, job_skills, job_description=""):
        """Calculate match score between user and job"""
        
        # Convert to lowercase
        user_skills_lower = [s.lower() for s in user_skills]
        job_skills_lower = [s.lower() for s in job_skills]
        
        # Find matching skills
        matching_skills = set(user_skills_lower) & set(job_skills_lower)
        
        # Calculate base score
        if not job_skills_lower:
            base_score = 50  # Default if no skills specified
        else:
            base_score = (len(matching_skills) / len(job_skills_lower)) * 70
        
        # Add weight bonus
        weight_bonus = sum(self.skill_weights.get(skill, 1) 
                          for skill in matching_skills 
                          if skill in self.skill_weights)
        
        # Calculate final score (0-100)
        final_score = min(base_score + (weight_bonus / 10), 100)
        
        return {
            'score': round(final_score),
            'matching_skills': list(matching_skills),
            'missing_skills': list(set(job_skills_lower) - set(user_skills_lower)),
            'explanation': self.generate_explanation(matching_skills, job_skills_lower)
        }
    
    def generate_explanation(self, matching_skills, job_skills):
        """Generate explanation for match score"""
        match_percent = (len(matching_skills) / len(job_skills)) * 100 if job_skills else 0
        
        if match_percent >= 80:
            return "🎯 Excellent match! You have most required skills."
        elif match_percent >= 60:
            return "✅ Good match. Consider learning 1-2 additional skills."
        elif match_percent >= 40:
            return "⚠️ Moderate match. Focus on missing skills."
        else:
            return "📚 Build more skills before applying."
    
    def recommend_improvements(self, user_skills, target_job):
        """Recommend skills to learn"""
        missing_skills = list(set(target_job['skills']) - set(user_skills))
        
        if not missing_skills:
            return "Great! You have all required skills."
        
        # Prioritize missing skills by importance
        prioritized = []
        for skill in missing_skills:
            weight = self.skill_weights.get(skill, 5)
            prioritized.append((skill, weight))
        
        prioritized.sort(key=lambda x: x[1], reverse=True)
        top_3 = [skill for skill, _ in prioritized[:3]]
        
        return {
            'skills_to_learn': top_3,
            'resources': self.get_learning_resources(top_3),
            'estimated_time': '2-4 weeks per skill'
        }
    
    def get_learning_resources(self, skills):
        """Get free learning resources for skills"""
        resources = {
            'python': ['freeCodeCamp Python', 'Codecademy Python', 'W3Schools Python'],
            'javascript': ['JavaScript.info', 'freeCodeCamp JavaScript', 'MDN Web Docs'],
            'react': ['React Official Tutorial', 'freeCodeCamp React', 'Scrimba React'],
            'sql': ['SQLZoo', 'Mode Analytics SQL', 'Khan Academy SQL'],
            'aws': ['AWS Free Tier', 'AWS Training', 'freeCodeCamp AWS']
        }
        
        result = {}
        for skill in skills:
            result[skill] = resources.get(skill, ['YouTube tutorials', 'Udemy free courses'])
        
        return result

# Test
if __name__ == "__main__":
    matcher = SimpleAIMatcher()
    
    user_skills = ['python', 'django', 'sql']
    job_skills = ['python', 'django', 'react', 'aws']
    
    result = matcher.calculate_match_score(user_skills, job_skills)
    print(f"Match Score: {result['score']}%")
    print(f"Matching: {result['matching_skills']}")
    print(f"Missing: {result['missing_skills']}")
    print(f"Explanation: {result['explanation']}")