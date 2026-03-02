import streamlit as st
import PyPDF2
import time
import random

# Page Config
st.set_page_config(page_title="CareerAI Pro", page_icon="🚀", layout="wide")

# Custom CSS for Premium Look
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgb(10, 15, 30) 0%, rgb(0, 5, 10) 90.2%);
    }
    .job-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s ease;
    }
    .job-card:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(0, 188, 212, 0.5);
    }
    .platform-badge {
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
    }
    .linkedin { background: #0077B5; color: white; }
    .naukri { background: #FF7555; color: white; }
    .indeed { background: #2164f3; color: white; }
    .glassdoor { background: #00A300; color: white; }
    
    .match-score {
        font-size: 24px;
        font-weight: bold;
        color: #00BDD4;
    }
    .skill-tag {
        background: rgba(0, 188, 212, 0.1);
        color: #00BDD4;
        padding: 2px 8px;
        border-radius: 4px;
        margin-right: 5px;
        font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar - History & Chat
with st.sidebar:
    st.markdown("<h1 style='color: #00BDD4;'>🚀 CareerAI Pro</h1>", unsafe_allow_html=True)
    st.divider()
    
    st.header("📋 History")
    if "history" not in st.session_state:
        st.session_state.history = []
    
    if st.session_state.history:
        for i, item in enumerate(st.session_state.history[-5:]):
            st.write(f"{i+1}. {item}")
    else:
        st.write("No history yet")
    
    st.divider()
    
    # Chat section
    st.header("💬 Career Chat")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask about careers, jobs, or skills..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Simple responses
        if "python" in prompt.lower():
            response = "Python is a great skill! It's used in web development, data science, AI, and automation. Consider building projects like a web scraper or data analyzer."
        elif "job" in prompt.lower():
            response = "I can help you find jobs! Upload your resume to get personalized suggestions, or create a new one using the 'Create Resume' tab."
        elif "skill" in prompt.lower():
            response = "Key in-demand skills include: Python, JavaScript, SQL, React, and cloud platforms like AWS. What skills do you have?"
        elif "internship" in prompt.lower():
            response = "Internships are crucial for experience! Check LinkedIn, company websites, and university job portals. Focus on roles that match your skills."
        else:
            response = "I'm here to help with your career journey! Try asking about specific skills, jobs, or resume tips."
        
        # Add assistant response
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Add to history
        st.session_state.history.append(f"Asked: {prompt[:30]}...")

st.title("🎯 AI Career & Opportunity Navigator")
st.write("Leveraging AI to bridge the gap between your skills and global opportunities.")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📄 Upload Resume", 
    "📝 Create Resume", 
    "📊 Analytics", 
    "🤖 AI Suggestions", 
    "🔍 AI Job Searcher"
])

# Upload Tab
with tab1:
    st.subheader("Step 1: Upload Your Resume")
    resume = st.file_uploader("Choose PDF file", type=['pdf'])

if resume:
    # Step 2: Read PDF
    pdf_reader = PyPDF2.PdfReader(resume)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    # Store for analytics
    st.session_state.resume_text = text
    
    # Step 3: Enhanced skill finder
    skills = []
    
    # Programming languages
    lang_skills = [
        ("python", "Python"), ("java", "Java"), ("javascript", "JavaScript"),
        ("c++", "C++"), ("c#", "C#"), ("go", "Go"), ("rust", "Rust"),
        ("php", "PHP"), ("ruby", "Ruby"), ("swift", "Swift")
    ]
    
    # Frameworks & libraries
    framework_skills = [
        ("react", "React"), ("vue", "Vue.js"), ("angular", "Angular"),
        ("django", "Django"), ("flask", "Flask"), ("spring", "Spring"),
        ("node.js", "Node.js"), ("express", "Express")
    ]
    
    # Databases
    db_skills = [
        ("sql", "SQL"), ("mysql", "MySQL"), ("postgresql", "PostgreSQL"),
        ("mongodb", "MongoDB"), ("redis", "Redis"), ("oracle", "Oracle")
    ]
    
    # Cloud & DevOps
    cloud_skills = [
        ("aws", "AWS"), ("azure", "Azure"), ("gcp", "Google Cloud"),
        ("docker", "Docker"), ("kubernetes", "Kubernetes"), ("jenkins", "Jenkins"),
        ("git", "Git"), ("linux", "Linux"), ("bash", "Bash")
    ]
    
    # Data & AI
    data_skills = [
        ("pandas", "Pandas"), ("numpy", "NumPy"), ("tensorflow", "TensorFlow"),
        ("pytorch", "PyTorch"), ("scikit-learn", "Scikit-learn"), ("r", "R"),
        ("tableau", "Tableau"), ("power bi", "Power BI")
    ]
    
    # Check all skill categories
    all_skills_list = lang_skills + framework_skills + db_skills + cloud_skills + data_skills
    
    for skill_key, skill_name in all_skills_list:
        if skill_key in text.lower():
            if skill_name not in skills:
                skills.append(skill_name)
    
    st.session_state.current_skills = skills
    
    # Step 4: Show results
    st.success("✅ Resume analyzed!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Your Skills")
        if skills:
            cols = st.columns(3)
            for i, skill in enumerate(skills):
                cols[i % 3].markdown(f"<span class='skill-tag'>{skill}</span>", unsafe_allow_html=True)
        else:
            st.write("No skills found. Add 'Skills' section to resume!")
    
    with col2:
        st.subheader("Profile Score")
        score = len(skills) * 10 if skills else 0
        score = min(score, 100)
        st.progress(score/100)
        st.write(f"{score}% optimization level")
    
    # Step 5: Show jobs
    st.divider()
    st.subheader("🎯 Quick Suggested Jobs")
    
    # Dynamic job suggestions based on skills
    job_templates = [
        {"company": "TechStart", "role": "Python Intern", "match": 85, "req": "Python, SQL, Problem Solving"},
        {"company": "WebCorp", "role": "Web Developer", "match": 70, "req": "JavaScript, React, HTML/CSS"},
        {"company": "DataCo", "role": "Data Analyst", "match": 60, "req": "Python, SQL, Statistics"},
        {"company": "CloudTech", "role": "DevOps Engineer", "match": 65, "req": "AWS, Docker, Linux"},
        {"company": "AICorp", "role": "ML Engineer", "match": 75, "req": "Python, TensorFlow, Mathematics"},
        {"company": "MobileDev", "role": "App Developer", "match": 55, "req": "Java, Android, Kotlin"},
        {"company": "CyberSec", "role": "Security Analyst", "match": 50, "req": "Linux, Networking, Python"},
        {"company": "GameStudio", "role": "Game Developer", "match": 45, "req": "C++, Unity, 3D Graphics"}
    ]
    
    # Filter jobs based on skills
    matched_jobs = []
    for job in job_templates:
        req_skills = job["req"].lower().split(", ")
        match_count = sum(1 for skill in req_skills if any(user_skill.lower() in skill for user_skill in skills))
        if match_count > 0 or len(skills) == 0:  # Show all if no skills found
            job["match"] = min(95, 50 + match_count * 15)  # Dynamic match percentage
            matched_jobs.append(job)
    
    # Sort by match percentage
    matched_jobs.sort(key=lambda x: x["match"], reverse=True)
    
    # Show top 4 jobs
    jobs = matched_jobs[:4]
    
    cols = st.columns(2)
    for i, job in enumerate(jobs):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="job-card">
                <h3>{job['role']}</h3>
                <p><strong>{job['company']}</strong></p>
                <p class="match-score">{job['match']}% Match</p>
                <p>Requirements: {job['req']}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"⚡ Apply to {job['company']}", key=f"quick_{i}"):
                st.success(f"Application sent to {job['company']}!")
    
    # Step 6: Tips
    st.subheader("💡 Tips to Improve")
    if len(skills) < 2:
        st.write("• Add more skills to your resume")
    if "intern" not in text.lower():
        st.write("• Look for internships on LinkedIn")
    st.write("• Build 2 projects for your portfolio")
    
    # Add to history
    resume_name = "User"
    if "name" in text.lower():
        lines = text.split("\n")
        for line in lines:
            if "name" in line.lower() and len(line.strip()) > 5:
                resume_name = line.split(":")[-1].strip()
                break
    
    history_entry = f"Analyzed {resume_name}'s resume ({len(skills)} skills)"
    if history_entry not in st.session_state.history:
        st.session_state.history.append(history_entry)

else:
    st.info("👆 Upload your resume to get started")

# Create Resume Tab
with tab2:
    st.subheader("📝 Professional Resume Builder")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
    
    with col2:
        degree = st.text_input("Degree")
        college = st.text_input("College/University")
        year = st.text_input("Year of Passing")
    
    skills_input = st.text_input("Skills (comma separated)")
    
    col3, col4 = st.columns(2)
    with col3:
        company = st.text_input("Recent Company")
        role = st.text_input("Role")
    with col4:
        duration = st.text_input("Duration")
    
    if st.button("✨ Generate AI Resume"):
        if name and email and skills_input:
            # Create resume content
            resume_content = f"""
=========================================
{name.upper()}
{email} | {phone}
=========================================

EDUCATION
---------
{degree} - {college} ({year})

SKILLS
------
{skills_input}

EXPERIENCE
----------
{role} at {company} ({duration})
=========================================
            """
            
            st.success("✅ Professional resume generated!")
            st.text_area("Your Compiled Resume", resume_content, height=350)
            
            # Add to history
            st.session_state.history.append(f"Generated resume for {name}")
            
            # Option to download
            st.download_button(
                "💾 Download as TXT", 
                resume_content, 
                file_name=f"{name}_resume.txt",
                mime="text/plain"
            )
        else:
            st.error("Please fill required fields (Name, Email, Skills)")

# Analytics Tab
with tab3:
    st.header("📊 Advanced Resume Analytics")
    
    if "resume_text" in st.session_state:
        text = st.session_state.resume_text
        
        # Skill analysis
        st.subheader("🛠️ Technical Skill Insights")
        
        # All possible skills for comparison
        all_possible_skills = [
            "Python", "Java", "JavaScript", "C++", "C#", "Go", "Rust", "PHP", "Ruby", "Swift",
            "React", "Vue.js", "Angular", "Django", "Flask", "Spring", "Node.js", "Express",
            "SQL", "MySQL", "PostgreSQL", "MongoDB", "Redis", "Oracle",
            "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "Jenkins", "Git", "Linux", "Bash",
            "Pandas", "NumPy", "TensorFlow", "PyTorch", "Scikit-learn", "R", "Tableau", "Power BI"
        ]
        
        # Find skills in resume
        found_skills = []
        for skill in all_possible_skills:
            if skill.lower() in text.lower():
                found_skills.append(skill)
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Detected Strengths:**")
            if found_skills:
                for skill in found_skills:
                    st.success(f"✔ {skill}")
            else:
                st.warning("No technical skills detected.")
        
        with col2:
            st.write("**Market Gaps (Top 10):**")
            missing = [skill for skill in all_possible_skills if skill not in found_skills]
            for skill in missing[:10]:
                st.error(f"✖ {skill}")
        
        # Resume score
        st.divider()
        st.subheader("📈 AI Readiness Score")
        score = 0
        if len(found_skills) > 0: score += 30
        if any(x in text.lower() for x in ["experience", "work", "intern"]): score += 25
        if "education" in text.lower(): score += 20
        if any(x in text.lower() for x in ["project", "portfolio"]): score += 25
        
        c1, c2 = st.columns([1, 2])
        with c1:
            st.metric("Total Score", f"{score}/100")
        with c2:
            st.progress(score/100)
        
        # Improvement suggestions
        st.subheader("🚀 Roadmap to 100")
        suggestions = []
        if len(found_skills) < 5:
            suggestions.append("Master at least 2 more in-demand frameworks.")
        if "project" not in text.lower():
            suggestions.append("Add a GitHub link with at least 3 live projects.")
        if len(text.split()) < 350:
            suggestions.append("Elaborate on your roles - aim for more descriptive bullet points.")
        if "linkedin" not in text.lower():
            suggestions.append("Integrate your LinkedIn profile for better reach.")
        
        for suggestion in suggestions:
            st.info(suggestion)
            
    else:
        st.info("Upload your profile to see deep analytics.")

# AI Suggestions Tab
with tab4:
    st.header("🤖 Personalized Career Roadmap")
    
    if "resume_text" in st.session_state:
        text = st.session_state.resume_text
        current_skills = st.session_state.get("current_skills", [])
        
        st.subheader("🌈 Recommended Career Paths")
        
        learning_paths = [
            {
                "title": "Full Stack Architect",
                "skills": ["React", "Node.js", "MongoDB", "AWS"],
                "description": "Design end-to-end scalable web systems.",
                "platforms": ["LinkedIn", "Indeed"]
            },
            {
                "title": "AI/ML Engineer",
                "skills": ["Python", "TensorFlow", "Math", "Scikit-learn"],
                "description": "Build intelligent predictive models.",
                "platforms": ["Kaggle Jobs", "AngelList"]
            },
            {
                "title": "Cloud Ops Specialist",
                "skills": ["AWS", "Kubernetes", "Docker", "Terraform"],
                "description": "Orchestrate global cloud infrastructures.",
                "platforms": ["LinkedIn", "CloudJobBoard"]
            }
        ]
        
        for path in learning_paths:
            with st.expander(f"💎 {path['title']}"):
                st.write(path['description'])
                st.write("**Skill Gap:**")
                for s in path['skills']:
                    if s in current_skills:
                        st.write(f"✅ {s}")
                    else:
                        st.write(f"⭕ {s} (Missing)")
                st.write("**Recommended Platforms:**", ", ".join(path['platforms']))
                
    else:
        st.info("Please upload your resume to generate a custom roadmap.")

# NEW: AI Job Searcher Tab
with tab5:
    st.header("🔍 AI Real-time Job Opportunity Finder")
    st.write("Scan global job markets (LinkedIn, Naukri, Indeed, etc.) based on your unique profile.")
    
    if "resume_text" in st.session_state:
        current_skills = st.session_state.get("current_skills", [])
        
        if st.button("🚀 Scan Global Job Markets Now"):
            with st.spinner("AI is analyzing millions of postings..."):
                time.sleep(2)
                st.balloons()
                
                # Mock results for different platforms
                opportunities = [
                    {
                        "platform": "LinkedIn",
                        "title": "Junior Software Engineer",
                        "company": "Innovation Labs",
                        "match": random.randint(85, 98),
                        "tags": ["Remote", "Full-time", "Growth"],
                        "skills": current_skills[:2] + ["System Design"],
                        "url": "https://linkedin.com/jobs"
                    },
                    {
                        "platform": "Naukri",
                        "title": "Frontend Developer (React)",
                        "company": "Web Solutions Inc.",
                        "match": random.randint(80, 95),
                        "tags": ["Hybrid", "High Pay", "Immediate"],
                        "skills": ["React", "CSS", "TypeScript"],
                        "url": "https://naukri.com"
                    },
                    {
                        "platform": "Indeed",
                        "title": "Python Developer",
                        "company": "Data Insights Corp",
                        "match": random.randint(75, 92),
                        "tags": ["On-site", "MNC", "Benefits"],
                        "skills": ["Python", "SQL", "Pandas"],
                        "url": "https://indeed.com"
                    },
                    {
                        "platform": "Glassdoor",
                        "title": "Full Stack Intern",
                        "company": "Startup Hub",
                        "match": random.randint(90, 99),
                        "tags": ["Flexible", "Equity", "Fast-paced"],
                        "skills": current_skills[:3],
                        "url": "https://glassdoor.com"
                    }
                ]
                
                # Sort by match
                opportunities.sort(key=lambda x: x["match"], reverse=True)
                
                st.write(f"### Found {len(opportunities)} Top Matches for You")
                
                for opt in opportunities:
                    platform_class = opt['platform'].lower()
                    st.markdown(f"""
                    <div class="job-card">
                        <div style="display: flex; justify-content: space-between; align-items: start;">
                            <div>
                                <span class="platform-badge {platform_class}">{opt['platform']}</span>
                                <h2 style='margin: 10px 0;'>{opt['title']}</h2>
                                <h4 style='color: #888;'>{opt['company']}</h4>
                            </div>
                            <div style="text-align: right;">
                                <div class="match-score">{opt['match']}%</div>
                                <div style="font-size: 12px; color: #00BDD4;">AI MATCH</div>
                            </div>
                        </div>
                        <div style="margin: 15px 0;">
                            {' '.join([f'<span class="skill-tag">{s}</span>' for s in opt['tags']])}
                        </div>
                        <div style="margin-bottom: 15px;">
                            <strong>Required Keywords:</strong><br>
                            {' '.join([f'<span style="font-size: 12px; color: #eee; margin-right:8px;">• {s}</span>' for s in opt['skills']])}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"Go to {opt['platform']} Listing", key=f"btn_{opt['platform']}_{opt['title']}"):
                        st.info(f"Redirecting to {opt['url']}...")

                # Related Opportunities Section
                st.divider()
                st.subheader("💡 Related Growth Opportunities")
                st.write("Filling these gaps can increase your match rate to 100%.")
                
                cert_cols = st.columns(3)
                certs = [
                    {"name": "AWS Certified Developer", "platform": "Coursera", "relevance": "High"},
                    {"name": "Advanced React Patterns", "platform": "Udemy", "relevance": "Medium"},
                    {"name": "Python for Data Science", "platform": "edX", "relevance": "High"}
                ]
                for i, cert in enumerate(certs):
                    with cert_cols[i % 3]:
                        st.markdown(f"""
                        <div style="background: rgba(255,255,255,0.03); padding: 15px; border-radius: 10px; border: 1px dashed rgba(0,188,212,0.3);">
                            <h4 style="margin:0;">{cert['name']}</h4>
                            <p style="font-size: 12px; color: #888;">{cert['platform']} • <b>{cert['relevance']} Relevance</b></p>
                        </div>
                        """, unsafe_allow_html=True)
                        if st.button("Enroll Now", key=f"cert_{i}"):
                            st.success(f"Opening {cert['platform']} course...")
        
        else:
            st.info("Click the button above to start searching for opportunities across LinkedIn, Naukri, and more.")
    
    else:
        st.warning("⚠️ Please upload your resume in the first tab to use the AI Job Searcher.")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #888;">
    <p>Built with ❤️ by BUNNY RANGU | Advanced AI Career Assistant</p>
    <p>Contact: <a href="mailto:bunnyrangu29@gmail.com" style="color: #00BDD4;">bunnyrangu29@gmail.com</a></p>
</div>
""", unsafe_allow_html=True)

