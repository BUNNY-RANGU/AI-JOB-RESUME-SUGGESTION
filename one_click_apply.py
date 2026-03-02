import streamlit as st
import json

class OneClickApply:
    """Naukri-style one-click application system"""
    
    def __init__(self):
        self.user_profile = {}
        self.load_user_profile()
    
    def load_user_profile(self):
        """Load user profile for autofill"""
        try:
            with open("user_profile.json", "r") as f:
                self.user_profile = json.load(f)
        except:
            self.user_profile = {
                'name': '',
                'email': '',
                'phone': '',
                'resume_path': '',
                'cover_letter_template': ''
            }
    
    def create_quick_apply_modal(self, job_id, job_title, company):
        """Create popup modal for quick apply"""
        
        modal_html = f"""
        <div id="applyModal" style="
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            z-index: 10000;
            width: 90%;
            max-width: 500px;
            display: none;
        ">
            <h3 style="margin-top: 0;">⚡ Quick Apply: {job_title}</h3>
            <p style="color: #666; margin-bottom: 20px;">at <strong>{company}</strong></p>
            
            <div style="margin-bottom: 20px;">
                <label style="display: block; margin-bottom: 5px; font-weight: 500;">Your Name</label>
                <input type="text" id="applicantName" value="{self.user_profile.get('name', '')}" 
                       style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 8px;">
            </div>
            
            <div style="margin-bottom: 20px;">
                <label style="display: block; margin-bottom: 5px; font-weight: 500;">Email</label>
                <input type="email" id="applicantEmail" value="{self.user_profile.get('email', '')}" 
                       style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 8px;">
            </div>
            
            <div style="margin-bottom: 25px;">
                <label style="display: block; margin-bottom: 5px; font-weight: 500;">Cover Letter</label>
                <textarea id="coverLetter" rows="4" style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 8px;">
{self.generate_cover_letter(job_title, company)}
                </textarea>
            </div>
            
            <div style="display: flex; gap: 10px;">
                <button onclick="submitApplication({job_id})" style="
                    flex: 1;
                    background: linear-gradient(135deg, #10b981, #059669);
                    color: white;
                    border: none;
                    padding: 12px;
                    border-radius: 8px;
                    font-weight: 600;
                    cursor: pointer;
                ">
                    ✅ Submit Application
                </button>
                <button onclick="closeModal()" style="
                    flex: 1;
                    background: #ef4444;
                    color: white;
                    border: none;
                    padding: 12px;
                    border-radius: 8px;
                    font-weight: 600;
                    cursor: pointer;
                ">
                    ❌ Cancel
                </button>
            </div>
        </div>
        
        <div id="overlay" style="
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 9999;
            display: none;
        "></div>
        
        <script>
        function showApplyModal() {{
            document.getElementById('applyModal').style.display = 'block';
            document.getElementById('overlay').style.display = 'block';
        }}
        
        function closeModal() {{
            document.getElementById('applyModal').style.display = 'none';
            document.getElementById('overlay').style.display = 'none';
        }}
        
        function submitApplication(jobId) {{
            const name = document.getElementById('applicantName').value;
            const email = document.getElementById('applicantEmail').value;
            const coverLetter = document.getElementById('coverLetter').value;
            
            // Show success animation
            document.getElementById('applyModal').innerHTML = `
                <div style="text-align: center; padding: 40px;">
                    <div style="font-size: 60px; color: #10b981;">🎯</div>
                    <h3>Application Submitted!</h3>
                    <p>Good luck with your application at {company}!</p>
                    <p style="font-size: 12px; color: #666;">You'll receive confirmation at: ${{email}}</p>
                    <button onclick="closeModal()" style="
                        margin-top: 20px;
                        padding: 10px 20px;
                        background: #3b82f6;
                        color: white;
                        border: none;
                        border-radius: 8px;
                        cursor: pointer;
                    ">
                        Close
                    </button>
                </div>
            `;
            
            // In production, this would send data to backend
            console.log("Application submitted for job:", jobId);
        }}
        
        // Show modal when page loads (for demo)
        window.onload = showApplyModal;
        </script>
        """
        
        st.markdown(modal_html, unsafe_allow_html=True)
    
    def generate_cover_letter(self, job_title, company):
        """Generate personalized cover letter"""
        template = f"""Dear Hiring Manager,

I am writing to express my interest in the {job_title} position at {company}. 

Based on my skills and experience, I believe I would be a strong fit for this role.

Looking forward to the opportunity to contribute to your team.

Sincerely,
{self.user_profile.get('name', '[Your Name]')}"""
        
        return template
    
    def create_quick_apply_button(self, job_id, job_title, company):
        """Create one-click apply button"""
        
        button_html = f"""
        <button onclick="showApplyModal({job_id})" style="
            background: linear-gradient(135deg, #10b981, #059669);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s;
            width: 100%;
            justify-content: center;
        ">
            ⚡ Easy Apply
        </button>
        
        <script>
        function showApplyModal(jobId) {{
            // This would trigger the modal
            alert("Applying to {job_title} at {company}");
            // In production, this would open the actual modal
        }}
        </script>
        """
        
        return button_html