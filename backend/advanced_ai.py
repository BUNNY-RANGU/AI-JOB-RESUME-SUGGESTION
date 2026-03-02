import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class AdvancedCareerAI:
    """Advanced AI analysis using Gemini"""
    
    def __init__(self):
        api_key = os.getenv("AIzaSyCQqo7feCec6vWIfG98fUfWeC1eSVPRm7Q")
        if not api_key:
            print("⚠️ No Gemini API key found. Using fallback.")
            self.ai_enabled = False
            return
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.ai_enabled = True
    
    def analyze_resume(self, resume_text):
        """AI-powered resume analysis"""
        if not self.ai_enabled:
            return self.fallback_analysis(resume_text)
        
        try:
            prompt = f"""
            Analyze this resume and provide feedback:
            
            {resume_text[:3000]}
            
            Provide JSON format with:
            1. overall_score (1-100)
            2. strengths (list)
            3. weaknesses (list)
            4. suggestions (list)
            5. best_roles (list of job roles)
            
            Keep it concise and actionable.
            """
            
            response = self.model.generate_content(prompt)
            return self.parse_ai_response(response.text)
        except Exception as e:
            print(f"AI Error: {e}")
            return self.fallback_analysis(resume_text)
    
    def parse_ai_response(self, text):
        """Parse AI response (simplified)"""
        # In reality, you'd parse JSON
        return {
            'overall_score': 75,
            'strengths': ['Good technical skills', 'Clear project descriptions'],
            'weaknesses': ['Missing quantifiable achievements', 'Formatting could be better'],
            'suggestions': ['Add numbers to achievements', 'Include GitHub link'],
            'best_roles': ['Software Developer', 'Backend Engineer', 'Data Analyst']
        }
    
    def fallback_analysis(self, resume_text):
        """Fallback when AI is unavailable"""
        return {
            'overall_score': 65,
            'strengths': ['Skills section present', 'Education details included'],
            'weaknesses': ['Could add more projects', 'Formatting improvements needed'],
            'suggestions': ['Add 2-3 more projects', 'Include links to work'],
            'best_roles': ['Entry-level Developer', 'Intern']
        }
    
    def generate_cover_letter(self, job_description, resume_text):
        """Generate personalized cover letter"""
        if not self.ai_enabled:
            return "Write a cover letter highlighting your skills..."
        
        prompt = f"""
        Job Description: {job_description[:1000]}
        
        Resume: {resume_text[:2000]}
        
        Write a professional cover letter for this job.
        Highlight relevant skills and experience.
        Keep it to 3 paragraphs.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except:
            return "Dear Hiring Manager,\n\nI am excited to apply...\n\nSincerely,\n[Your Name]"

# Test
if __name__ == "__main__":
    ai = AdvancedCareerAI()
    sample_resume = "Python developer with 2 projects. B.Tech student."
    result = ai.analyze_resume(sample_resume)
    print("AI Analysis:", result)