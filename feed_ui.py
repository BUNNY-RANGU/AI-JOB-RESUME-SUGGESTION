import streamlit as st
import time
import random
from datetime import datetime

class AddictiveJobFeed:
    """Create LinkedIn-like endless job feed"""
    
    def __init__(self):
        self.jobs_per_page = 5
        self.current_page = 0
    
    def create_job_card(self, job, index):
        """Create swipeable job card"""
        
        # LinkedIn-like card design
        card_html = f"""
        <div class="job-card" id="job-{index}">
            <div style="display: flex; align-items: start; margin-bottom: 15px;">
                <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                     border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 15px;">
                    <span style="color: white; font-size: 20px;">{job['company'][0]}</span>
                </div>
                <div style="flex: 1;">
                    <h3 style="margin: 0; color: #1a1a1a; font-size: 18px;">{job['title']}</h3>
                    <p style="margin: 5px 0; color: #666; font-size: 14px;">
                        <strong>{job['company']}</strong> • {job['location']} • {job.get('type', 'Full-time')}
                    </p>
                    <p style="margin: 5px 0; color: #666; font-size: 12px;">
                        ⏱️ Posted {job.get('time_ago', 'Recently')} • 🔥 {job.get('applicants', 'Few')} applicants
                    </p>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 24px; color: #10b981; font-weight: bold;">{job['match']}%</div>
                    <div style="font-size: 10px; color: #666;">Match</div>
                </div>
            </div>
            
            <div style="background: #f8f9fa; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <div style="display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 8px;">
                    {''.join([f'<span class="skill-tag">{skill}</span>' for skill in job['skills'][:5]])}
                </div>
                <p style="margin: 0; color: #444; font-size: 14px; line-height: 1.4;">
                    {job['description'][:150]}...
                </p>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-top: 15px;">
                <button class="action-btn" onclick="handleSave({index})" style="background: #3b82f6;">
                    💾 Save
                </button>
                <button class="action-btn" onclick="handleApply({index})" style="background: #10b981;">
                    ⚡ Easy Apply
                </button>
                <button class="action-btn" onclick="handleDetails({index})" style="background: #8b5cf6;">
                    📊 Details
                </button>
            </div>
        </div>
        <div style="height: 20px;"></div>
        """
        return card_html
    
    def create_feed_ui(self):
        """Create the main feed interface"""
        
        # Custom CSS for addictive design
        st.markdown("""
        <style>
        /* LinkedIn-inspired design */
        .job-card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin: 15px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border: 1px solid #e6e6e6;
            transition: all 0.3s ease;
        }
        
        .job-card:hover {
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            transform: translateY(-2px);
        }
        
        .skill-tag {
            background: #e0f2fe;
            color: #0369a1;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .action-btn {
            border: none;
            padding: 10px;
            border-radius: 8px;
            color: white;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            width: 100%;
        }
        
        .action-btn:hover {
            opacity: 0.9;
            transform: scale(1.02);
        }
        
        /* Progress bar */
        .progress-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: #f0f0f0;
            z-index: 1000;
        }
        
        .progress-bar {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            width: 0%;
            transition: width 0.3s;
        }
        
        /* Floating action button */
        .fab {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 24px;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            cursor: pointer;
            z-index: 1000;
        }
        </style>
        
        <!-- Progress Bar -->
        <div class="progress-container">
            <div class="progress-bar" id="progressBar"></div>
        </div>
        
        <!-- Floating Action Button -->
        <div class="fab" onclick="refreshFeed()">
            🔄
        </div>
        
        <script>
        // Update progress bar on scroll
        window.onscroll = function() {
            var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            var scrolled = (winScroll / height) * 100;
            document.getElementById("progressBar").style.width = scrolled + "%";
        };
        
        // Auto-refresh when near bottom
        window.onscroll = function() {
            if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 500) {
                loadMoreJobs();
            }
        };
        
        function loadMoreJobs() {
            // This would trigger Streamlit to load more jobs
            console.log("Loading more jobs...");
        }
        
        function handleSave(jobId) {
            alert("Job saved to your list!");
        }
        
        function handleApply(jobId) {
            alert("Applied successfully! Good luck! 🎯");
        }
        
        function handleDetails(jobId) {
            alert("Showing detailed view for job " + jobId);
        }
        
        function refreshFeed() {
            location.reload();
        }
        </script>
        """, unsafe_allow_html=True)
        
        # Main feed header
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            st.markdown("### 🎯 Your Job Feed")
            st.caption("Personalized jobs based on your profile")
        
        with col2:
            if st.button("⚙️ Filters", use_container_width=True):
                st.session_state.show_filters = not st.session_state.get('show_filters', False)
        
        with col3:
            if st.button("🔄 Refresh", type="primary", use_container_width=True):
                st.rerun()
        
        # Filters (collapsible)
        if st.session_state.get('show_filters', False):
            with st.expander("🔍 Filter Jobs", expanded=True):
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    job_type = st.multiselect("Job Type", ["Internship", "Full-time", "Part-time", "Remote"])
                with col2:
                    experience = st.select_slider("Experience", ["Fresher", "0-2 years", "2-5 years", "5+ years"])
                with col3:
                    salary_range = st.slider("Salary (LPA)", 0, 50, (5, 20))
                with col4:
                    location = st.multiselect("Location", ["Remote", "Bangalore", "Hyderabad", "Delhi", "Pune"])
        
        # Infinite scroll feed
        feed_container = st.container()
        
        with feed_container:
            # Generate sample jobs (in production, these would be from database)
            jobs = self.generate_sample_jobs()
            
            # Display job cards
            for i, job in enumerate(jobs):
                job_html = self.create_job_card(job, i)
                st.markdown(job_html, unsafe_allow_html=True)
            
            # Load more button
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("👇 Load More Jobs", use_container_width=True):
                    # In production, this would load next page
                    st.success("Loading more jobs...")
                    time.sleep(0.5)
                    st.rerun()
    
    def generate_sample_jobs(self):
        """Generate sample jobs for demo"""
        companies = ["Google", "Microsoft", "Amazon", "Flipkart", "Swiggy", "Zomato", "Infosys", "TCS"]
        locations = ["Remote", "Bangalore", "Hyderabad", "Pune", "Delhi NCR"]
        
        jobs = []
        for i in range(10):
            jobs.append({
                'title': random.choice(["Python Developer", "Frontend Engineer", "Data Analyst", 
                                       "DevOps Engineer", "Full Stack Developer"]),
                'company': random.choice(companies),
                'location': random.choice(locations),
                'type': random.choice(["Internship", "Full-time"]),
                'match': random.randint(65, 95),
                'skills': random.sample(["Python", "React", "AWS", "Docker", "SQL", "JavaScript", "Git"], 4),
                'description': "Looking for talented developers to join our team. Must have strong problem-solving skills and passion for technology.",
                'time_ago': random.choice(["Just now", "1 hour ago", "Today", "Yesterday"]),
                'applicants': random.choice(["Few", "50+", "100+", "200+"])
            })
        return jobs

# Usage
if __name__ == "__main__":
    feed = AddictiveJobFeed()
    feed.create_feed_ui()