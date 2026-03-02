import streamlit as st
import time
from datetime import datetime, timedelta

class CareerGamification:
    """Add LinkedIn-style gamification"""
    
    def __init__(self):
        self.streak_days = 0
        self.points = 100
        self.level = 1
    
    def create_profile_completeness(self):
        """Create profile progress bar"""
        
        completeness = 65  # Calculate based on user data
        
        html = f"""
        <div style="
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        ">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                <h4 style="margin: 0;">🏆 Profile Strength</h4>
                <span style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; 
                      padding: 4px 12px; border-radius: 20px; font-size: 12px;">
                    Level {self.level}
                </span>
            </div>
            
            <div style="margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <span style="font-size: 12px; color: #666;">Complete your profile to get better matches</span>
                    <span style="font-size: 14px; font-weight: 600; color: #3b82f6;">{completeness}%</span>
                </div>
                <div style="
                    width: 100%;
                    height: 8px;
                    background: #e5e7eb;
                    border-radius: 4px;
                    overflow: hidden;
                ">
                    <div style="
                        width: {completeness}%;
                        height: 100%;
                        background: linear-gradient(90deg, #667eea, #764ba2);
                        border-radius: 4px;
                        transition: width 0.5s;
                    "></div>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 20px;">
                <div style="text-align: center;">
                    <div style="font-size: 24px; font-weight: bold; color: #3b82f6;">{self.streak_days}</div>
                    <div style="font-size: 12px; color: #666;">🔥 Day Streak</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 24px; font-weight: bold; color: #10b981;">{self.points}</div>
                    <div style="font-size: 12px; color: #666;">⭐ Points</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 24px; font-weight: bold; color: #f59e0b;">12</div>
                    <div style="font-size: 12px; color: #666;">📊 Applications</div>
                </div>
            </div>
        </div>
        """
        
        st.markdown(html, unsafe_allow_html=True)
    
    def create_daily_challenge(self):
        """Create daily challenges"""
        
        challenges = [
            {"task": "Complete your profile", "points": 50, "completed": True},
            {"task": "Apply to 3 jobs", "points": 100, "completed": False},
            {"task": "Add 5 skills", "points": 75, "completed": False},
            {"task": "Upload resume", "points": 25, "completed": True},
        ]
        
        html = """
        <div style="
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        ">
            <h4 style="margin: 0 0 15px 0;">🎯 Daily Challenges</h4>
            <p style="color: #666; font-size: 14px; margin-bottom: 15px;">
                Complete challenges to earn points and level up!
            </p>
        """
        
        for i, challenge in enumerate(challenges):
            status = "✅" if challenge["completed"] else "◻️"
            color = "#10b981" if challenge["completed"] else "#3b82f6"
            
            html += f"""
            <div style="
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 10px 0;
                border-bottom: 1px solid #f0f0f0;
            ">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 20px; color: {color};">{status}</span>
                    <span style="font-size: 14px;">{challenge['task']}</span>
                </div>
                <span style="
                    background: {color};
                    color: white;
                    padding: 4px 12px;
                    border-radius: 20px;
                    font-size: 12px;
                    font-weight: 600;
                ">
                    +{challenge['points']} pts
                </span>
            </div>
            """
        
        html += """
        </div>
        """
        
        st.markdown(html, unsafe_allow_html=True)
    
    def create_achievements(self):
        """Display user achievements"""
        
        achievements = [
            {"icon": "🚀", "title": "First Application", "description": "Applied to your first job", "unlocked": True},
            {"icon": "🎯", "title": "Perfect Match", "description": "Found 95%+ match job", "unlocked": True},
            {"icon": "📈", "title": "Profile Pro", "description": "100% profile complete", "unlocked": False},
            {"icon": "🔥", "title": "7-Day Streak", "description": "Used app for 7 days straight", "unlocked": False},
        ]
        
        html = """
        <div style="
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        ">
            <h4 style="margin: 0 0 15px 0;">🏆 Achievements</h4>
            
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;">
        """
        
        for achievement in achievements:
            opacity = "1" if achievement["unlocked"] else "0.5"
            
            html += f"""
            <div style="
                background: #f8f9fa;
                border-radius: 10px;
                padding: 15px;
                opacity: {opacity};
            ">
                <div style="font-size: 24px; margin-bottom: 10px;">{achievement['icon']}</div>
                <div style="font-weight: 600; margin-bottom: 5px;">{achievement['title']}</div>
                <div style="font-size: 12px; color: #666;">{achievement['description']}</div>
            </div>
            """
        
        html += """
            </div>
        </div>
        """
        
        st.markdown(html, unsafe_allow_html=True)