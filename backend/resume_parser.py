import pdfplumber
import re
from typing import Dict, List

class SimpleResumeParser:
    """Basic resume parser for students"""
    
    def __init__(self):
        self.skills_keywords = {
            'programming': ['python', 'java', 'javascript', 'c++', 'c#', 'php', 'ruby', 'go'],
            'web': ['html', 'css', 'react', 'angular', 'vue', 'node', 'django', 'flask', 'spring'],
            'databases': ['sql', 'mysql', 'postgresql', 'mongodb', 'redis'],
            'cloud': ['aws', 'azure', 'gcp', 'docker', 'kubernetes'],
            'data_science': ['pandas', 'numpy', 'tensorflow', 'pytorch', 'ml', 'ai'],
            'tools': ['git', 'github', 'jenkins', 'jira', 'linux']
        }
    
    def extract_text(self, file_path: str) -> str:
        """Extract text from PDF or DOCX"""
        if file_path.endswith('.pdf'):
            with pdfplumber.open(file_path) as pdf:
                text = ''
                for page in pdf.pages:
                    text += page.extract_text()
                return text
        elif file_path.endswith('.docx'):
            import docx
            doc = docx.Document(file_path)
            return '\n'.join([para.text for para in doc.paragraphs])
        else:
            # Assume it's text file
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
    
    def extract_skills(self, text: str) -> List[str]:
        """Extract skills from resume text"""
        text_lower = text.lower()
        found_skills = []
        
        for category, skills in self.skills_keywords.items():
            for skill in skills:
                if skill in text_lower:
                    found_skills.append(skill)
        
        # Remove duplicates and return
        return list(set(found_skills))
    
    def extract_experience(self, text: str) -> Dict:
        """Extract experience information"""
        # Look for experience section
        lines = text.split('\n')
        experience_lines = []
        capture = False
        
        for line in lines:
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in ['experience', 'work', 'intern', 'project']):
                capture = True
            elif capture and line.strip() and not line.strip()[0].isdigit():
                experience_lines.append(line.strip())
        
        return {
            'summary': ' '.join(experience_lines[:3]),
            'has_internship': any(word in text.lower() for word in ['intern', 'training', 'practical']),
            'has_projects': any(word in text.lower() for word in ['project', 'github', 'portfolio'])
        }
    
    def parse_resume(self, file_path: str) -> Dict:
        """Main parsing function"""
        text = self.extract_text(file_path)
        
        return {
            'skills': self.extract_skills(text),
            'experience': self.extract_experience(text),
            'text_length': len(text),
            'education': self.extract_education(text),
            'extracted_text': text[:500] + '...'  # First 500 chars
        }
    
    def extract_education(self, text: str) -> str:
        """Extract education information"""
        lines = text.split('\n')
        for line in lines:
            line_lower = line.lower()
            if any(word in line_lower for word in ['b.tech', 'btech', 'engineering', 'degree', 'college']):
                return line.strip()[:100]
        return "Education details not found"

# Test the parser
if __name__ == "__main__":
    parser = SimpleResumeParser()
    # Create a sample text resume
    sample_text = """
    John Doe
    B.Tech Computer Science, IIT Delhi
    
    SKILLS:
    Python, JavaScript, React, SQL, AWS
    
    EXPERIENCE:
    Intern at Google - Built a web app using React and Python
    Project: E-commerce website with Django
    """
    
    with open("sample_resume.txt", "w") as f:
        f.write(sample_text)
    
    result = parser.parse_resume("sample_resume.txt")
    print("Parsed Resume:", result)