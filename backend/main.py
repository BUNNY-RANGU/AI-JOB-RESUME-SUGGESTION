"""
FastAPI Backend Server for AI Career Suggestion Platform
"""
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import backend modules
from database import CareerDatabase
from ai_matcher import SimpleAIMatcher
from resume_parser import SimpleResumeParser

app = FastAPI(title="AI Career Suggestion API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
db = CareerDatabase()
matcher = SimpleAIMatcher()
parser = SimpleResumeParser()

# Pydantic models
class UserProfile(BaseModel):
    email: str
    skills: List[str]
    resume_path: Optional[str] = None

class JobSearch(BaseModel):
    skills: List[str]
    location: Optional[str] = None

class JobMatchResponse(BaseModel):
    score: int
    matching_skills: List[str]
    missing_skills: List[str]
    explanation: str

# Routes
@app.get("/")
async def root():
    return {"message": "AI Career Suggestion API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "connected"}

@app.post("/api/profile")
async def create_profile(profile: UserProfile):
    """Create or update user profile"""
    try:
        user_id = db.save_user_profile(
            profile.email,
            profile.skills,
            profile.resume_path or ""
        )
        return {"user_id": user_id, "message": "Profile saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/resume/parse")
async def parse_resume(file: UploadFile = File(...)):
    """Parse uploaded resume"""
    try:
        # Save uploaded file temporarily
        import tempfile
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name
        
        # Parse resume
        result = parser.parse_resume(tmp_path)
        
        # Clean up
        os.unlink(tmp_path)
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing resume: {str(e)}")

@app.post("/api/jobs/match")
async def match_jobs(search: JobSearch):
    """Get matching jobs for user skills"""
    try:
        # Get jobs from database
        jobs = db.get_jobs_by_skills(search.skills)
        
        if not jobs:
            # Return sample jobs if database is empty
            jobs = [
                {
                    "title": "Python Developer Intern",
                    "company": "TechCorp Solutions",
                    "location": "Remote",
                    "skills_required": ["python", "django", "sql"],
                    "link": "https://example.com/job1",
                    "source": "naukri"
                },
                {
                    "title": "Frontend Developer",
                    "company": "WebStart Inc",
                    "location": "Bangalore",
                    "skills_required": ["javascript", "react", "html", "css"],
                    "link": "https://example.com/job2",
                    "source": "linkedin"
                },
                {
                    "title": "Data Analyst",
                    "company": "DataInsights",
                    "location": "Delhi",
                    "skills_required": ["python", "sql", "excel", "pandas"],
                    "link": "https://example.com/job3",
                    "source": "indeed"
                }
            ]
        
        # Calculate match scores
        results = []
        for job in jobs:
            match_result = matcher.calculate_match_score(
                search.skills,
                job.get("skills_required", [])
            )
            results.append({
                "job": job,
                "match": match_result
            })
        
        # Sort by score
        results.sort(key=lambda x: x["match"]["score"], reverse=True)
        
        return {"jobs": results[:10]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/jobs")
async def get_jobs(skills: str = ""):
    """Get all jobs or filter by skills"""
    try:
        skill_list = skills.split(",") if skills else []
        jobs = db.get_jobs_by_skills(skill_list)
        return {"jobs": jobs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/analyze/skills")
async def analyze_skills(text: str):
    """Analyze skills from text"""
    try:
        skills = parser.extract_skills(text)
        experience = parser.extract_experience(text)
        
        return {
            "skills": skills,
            "experience": experience
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/recommend")
async def get_recommendations(user_skills: List[str], target_job: dict):
    """Get skill recommendations"""
    try:
        recommendations = matcher.recommend_improvements(user_skills, target_job)
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Initialize database with sample data
@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    db.add_sample_data()
    print("✅ Database initialized with sample data")

if __name__ == "__main__":
    print("🚀 Starting AI Career Suggestion Backend...")
    print("📡 API available at http://localhost:8000")
    print("📚 Docs available at http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
