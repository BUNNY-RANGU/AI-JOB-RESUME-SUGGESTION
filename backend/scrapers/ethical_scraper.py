import requests
from bs4 import BeautifulSoup
import time
import random
from datetime import datetime

class EthicalJobScraper:
    """Scrape job listings ethically (for educational purposes)"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.delay = random.uniform(1, 3)  # Be polite
    
    def scrape_naukri_sample(self, skills="python"):
        """Scrape sample jobs (using Naukri's search page)"""
        try:
            # Note: In production, you'd use Naukri's API or get permission
            # This is a SIMULATION for educational purposes
            
            # Instead of actual scraping, we'll return sample data
            # This avoids legal issues while you learn
            
            sample_jobs = [
                {
                    'title': f'Python Developer Intern ({skills})',
                    'company': 'TechCorp India',
                    'location': 'Remote / Bangalore',
                    'skills': ['python', 'django', 'rest api'],
                    'link': '#',
                    'source': 'naukri_simulated',
                    'description': f'Looking for {skills} developer with Django experience'
                },
                {
                    'title': f'Junior {skills.title()} Developer',
                    'company': 'Startup Solutions',
                    'location': 'Hyderabad',
                    'skills': [skills, 'javascript', 'html', 'css'],
                    'link': '#',
                    'source': 'naukri_simulated',
                    'description': f'Entry level position for {skills} developers'
                }
            ]
            
            time.sleep(self.delay)  # Simulate delay
            return sample_jobs
            
        except Exception as e:
            print(f"Scraping error: {e}")
            return []
    
    def scrape_github_jobs(self):
        """Use GitHub Jobs API (public and free)"""
        try:
            url = "https://jobs.github.com/positions.json"
            response = requests.get(url, headers=self.headers)
            
            if response.status_code == 200:
                jobs = response.json()
                formatted_jobs = []
                
                for job in jobs[:5]:  # Limit to 5
                    formatted_jobs.append({
                        'title': job.get('title', ''),
                        'company': job.get('company', ''),
                        'location': job.get('location', 'Remote'),
                        'skills': self.extract_skills_from_desc(job.get('description', '')),
                        'link': job.get('url', '#'),
                        'source': 'github_jobs',
                        'description': job.get('description', '')[:200] + '...'
                    })
                
                return formatted_jobs
            return []
        except:
            return []
    
    def extract_skills_from_desc(self, description):
        """Extract skills from job description"""
        skills_keywords = ['python', 'java', 'javascript', 'react', 'node', 'sql', 
                          'aws', 'docker', 'git', 'html', 'css', 'django', 'flask']
        
        found_skills = []
        desc_lower = description.lower()
        
        for skill in skills_keywords:
            if skill in desc_lower:
                found_skills.append(skill)
        
        return found_skills[:5]
    
    def get_jobs_from_multiple_sources(self, skills="python"):
        """Get jobs from multiple sources"""
        all_jobs = []
        
        # Get GitHub jobs (real API)
        github_jobs = self.scrape_github_jobs()
        all_jobs.extend(github_jobs)
        
        # Get simulated Naukri jobs (for learning)
        naukri_jobs = self.scrape_naukri_sample(skills)
        all_jobs.extend(naukri_jobs)
        
        # Add timestamp
        for job in all_jobs:
            job['scraped_at'] = datetime.now().strftime('%Y-%m-%d %H:%M')
        
        return all_jobs

# Test
if __name__ == "__main__":
    scraper = EthicalJobScraper()
    jobs = scraper.get_jobs_from_multiple_sources("python")
    print(f"Found {len(jobs)} jobs")
    for job in jobs[:2]:
        print(f"- {job['title']} at {job['company']}")