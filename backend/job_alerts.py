import schedule
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import threading

class JobAlertSystem:
    """System for sending job alerts"""
    
    def __init__(self):
        self.users = {}  # In production, use database
    
    def add_user_alert(self, email, skills, frequency='daily'):
        """Add user to alert system"""
        self.users[email] = {
            'skills': skills,
            'frequency': frequency,
            'last_sent': None
        }
        return True
    
    def check_and_send_alerts(self):
        """Check and send alerts"""
        for email, info in self.users.items():
            if self.should_send_alert(info):
                jobs = self.find_recent_jobs(info['skills'])
                if jobs:
                    self.send_email_alert(email, jobs)
                    info['last_sent'] = datetime.now()
    
    def should_send_alert(self, user_info):
        """Check if should send alert based on frequency"""
        if not user_info['last_sent']:
            return True
        
        now = datetime.now()
        last = user_info['last_sent']
        
        if user_info['frequency'] == 'daily':
            return (now - last).days >= 1
        elif user_info['frequency'] == 'weekly':
            return (now - last).days >= 7
        
        return False
    
    def find_recent_jobs(self, skills):
        """Find recent jobs matching skills"""
        # Use your scraper here
        return [
            {"title": "Python Developer", "company": "Example Corp", "link": "#"},
            {"title": "Web Developer", "company": "Sample Inc", "link": "#"}
        ]
    
    def send_email_alert(self, email, jobs):
        """Send email alert"""
        # Simplified - in production, use real email
        print(f"Would send email to {email} with {len(jobs)} jobs")
        return True
    
    def start_background_scheduler(self):
        """Start background scheduler"""
        schedule.every().day.at("09:00").do(self.check_and_send_alerts)
        
        def run_scheduler():
            while True:
                schedule.run_pending()
                time.sleep(60)
        
        # Run in background thread
        thread = threading.Thread(target=run_scheduler, daemon=True)
        thread.start()
        print("✅ Job alert scheduler started")

# Test
if __name__ == "__main__":
    alerts = JobAlertSystem()
    alerts.add_user_alert("student@example.com", ["python", "javascript"])
    alerts.check_and_send_alerts()