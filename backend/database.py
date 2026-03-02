import sqlite3
import json
from datetime import datetime

class CareerDatabase:
    """Simple SQLite database for storing user data and jobs"""
    
    def __init__(self, db_path="career_data.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Users table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            skills TEXT,
            resume_path TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Jobs table (scraped jobs)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            skills_required TEXT,
            job_link TEXT,
            source TEXT,
            posted_date DATE,
            is_active BOOLEAN DEFAULT 1
        )
        ''')
        
        # Applications table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            job_id INTEGER,
            applied_date DATE,
            status TEXT DEFAULT 'applied',
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (job_id) REFERENCES jobs (id)
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_user_profile(self, email, skills, resume_path):
        """Save or update user profile"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT OR REPLACE INTO users (email, skills, resume_path)
        VALUES (?, ?, ?)
        ''', (email, json.dumps(skills), resume_path))
        
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        
        return user_id
    
    def save_job(self, job_data):
        """Save scraped job to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Check if job already exists
        cursor.execute('''
        SELECT id FROM jobs WHERE job_link = ?
        ''', (job_data['link'],))
        
        existing = cursor.fetchone()
        
        if not existing:
            cursor.execute('''
            INSERT INTO jobs (title, company, location, skills_required, job_link, source, posted_date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                job_data['title'],
                job_data['company'],
                job_data['location'],
                json.dumps(job_data.get('skills', [])),
                job_data['link'],
                job_data.get('source', 'unknown'),
                datetime.now().strftime('%Y-%m-%d')
            ))
        
        conn.commit()
        conn.close()
    
    def get_jobs_by_skills(self, skills_list, limit=20):
        """Get jobs matching user skills"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Simple keyword matching
        query = '''
        SELECT * FROM jobs 
        WHERE is_active = 1
        ORDER BY posted_date DESC
        LIMIT ?
        '''
        
        cursor.execute(query, (limit,))
        jobs = cursor.fetchall()
        
        # Convert to list of dicts
        job_list = []
        for job in jobs:
            job_dict = {
                'id': job[0],
                'title': job[1],
                'company': job[2],
                'location': job[3],
                'skills_required': json.loads(job[4]) if job[4] else [],
                'link': job[5],
                'source': job[6],
                'posted_date': job[7]
            }
            job_list.append(job_dict)
        
        conn.close()
        return job_list
    
    def add_sample_data(self):
        """Add sample jobs for testing"""
        sample_jobs = [
            {
                'title': 'Python Developer Intern',
                'company': 'TechCorp Solutions',
                'location': 'Remote',
                'skills': ['python', 'django', 'sql'],
                'link': 'https://example.com/job1',
                'source': 'naukri'
            },
            {
                'title': 'Frontend Developer',
                'company': 'WebStart Inc',
                'location': 'Bangalore',
                'skills': ['javascript', 'react', 'html', 'css'],
                'link': 'https://example.com/job2',
                'source': 'linkedin'
            },
            {
                'title': 'Data Analyst',
                'company': 'DataInsights',
                'location': 'Delhi',
                'skills': ['python', 'sql', 'excel', 'pandas'],
                'link': 'https://example.com/job3',
                'source': 'indeed'
            }
        ]
        
        for job in sample_jobs:
            self.save_job(job)
        
        print("✅ Added sample job data")

# Test
if __name__ == "__main__":
    db = CareerDatabase()
    db.add_sample_data()
    jobs = db.get_jobs_by_skills(['python'])
    print(f"Found {len(jobs)} jobs")