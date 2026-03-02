import streamlit as st
import asyncio
import time
from datetime import datetime

class SmartNotifications:
    """LinkedIn-style smart notifications"""
    
    def __init__(self):
        self.notifications = []
        self.load_notifications()
    
    def load_notifications(self):
        """Load user notifications"""
        # Sample notifications
        self.notifications = [
            {"type": "job_match", "message": "New job matches your Python skills!", "time": "2 min ago", "read": False},
            {"type": "application", "message": "Your application was viewed by Amazon", "time": "1 hour ago", "read": False},
            {"type": "profile", "message": "Your profile is 80% complete", "time": "3 hours ago", "read": True},
            {"type": "alert", "message": "Deadline approaching for Google internship", "time": "Yesterday", "read": True},
        ]
    
    def create_notification_bell(self):
        """Create notification bell with badge"""
        
        unread_count = sum(1 for n in self.notifications if not n["read"])
        
        html = f"""
        <style>
        .notification-bell {{
            position: relative;
            display: inline-block;
            cursor: pointer;
            font-size: 24px;
        }}
        
        .notification-badge {{
            position: absolute;
            top: -5px;
            right: -5px;
            background: #ef4444;
            color: white;
            border-radius: 50%;
            width: 18px;
            height: 18px;
            font-size: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .notification-dropdown {{
            display: none;
            position: absolute;
            right: 0;
            top: 100%;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            width: 350px;
            max-height: 400px;
            overflow-y: auto;
            z-index: 1000;
            margin-top: 10px;
        }}
        
        .notification-item {{
            padding: 15px;
            border-bottom: 1px solid #f0f0f0;
            cursor: pointer;
            transition: background 0.2s;
        }}
        
        .notification-item:hover {{
            background: #f8f9fa;
        }}
        
        .notification-item.unread {{
            background: #f0f9ff;
        }}
        </style>
        
        <div class="notification-bell" onclick="toggleNotifications()">
            🔔
            {f'<span class="notification-badge">{unread_count}</span>' if unread_count > 0 else ''}
            
            <div class="notification-dropdown" id="notificationDropdown">
                <div style="padding: 15px; border-bottom: 1px solid #f0f0f0;">
                    <strong>Notifications</strong>
                    <span style="float: right; font-size: 12px; color: #3b82f6; cursor: pointer;" 
                          onclick="markAllRead()">Mark all read</span>
                </div>
        """
        
        for notification in self.notifications[:5]:  # Show last 5
            unread_class = "unread" if not notification["read"] else ""
            
            html += f"""
            <div class="notification-item {unread_class}" onclick="handleNotificationClick()">
                <div style="font-size: 14px;">{notification['message']}</div>
                <div style="font-size: 11px; color: #666; margin-top: 5px;">{notification['time']}</div>
            </div>
            """
        
        html += """
                <div style="padding: 10px; text-align: center; border-top: 1px solid #f0f0f0;">
                    <a href="#" style="color: #3b82f6; text-decoration: none; font-size: 12px;">
                        See all notifications
                    </a>
                </div>
            </div>
        </div>
        
        <script>
        function toggleNotifications() {
            const dropdown = document.getElementById('notificationDropdown');
            dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
        }
        
        function markAllRead() {
            alert("All notifications marked as read!");
            // In production, this would call backend
        }
        
        function handleNotificationClick() {
            // Handle notification click
            console.log("Notification clicked");
        }
        
        // Close dropdown when clicking outside
        document.addEventListener('click', function(event) {
            const dropdown = document.getElementById('notificationDropdown');
            const bell = document.querySelector('.notification-bell');
            
            if (!bell.contains(event.target) && !dropdown.contains(event.target)) {
                dropdown.style.display = 'none';
            }
        });
        </script>
        """
        
        return html
    
    def create_push_notification(self, message, type="info"):
        """Create push notification"""
        
        colors = {
            "info": "#3b82f6",
            "success": "#10b981", 
            "warning": "#f59e0b",
            "error": "#ef4444"
        }
        
        html = f"""
        <div id="pushNotification" style="
            position: fixed;
            top: 20px;
            right: 20px;
            background: white;
            border-left: 4px solid {colors.get(type, '#3b82f6')};
            border-radius: 8px;
            padding: 15px 20px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.15);
            z-index: 10000;
            display: flex;
            align-items: center;
            gap: 10px;
            animation: slideIn 0.3s ease-out;
            max-width: 350px;
        ">
            <div style="font-size: 20px;">
                {'🔔' if type == 'info' else '✅' if type == 'success' else '⚠️' if type == 'warning' else '❌'}
            </div>
            <div style="flex: 1;">
                <div style="font-size: 14px; font-weight: 500;">{message}</div>
            </div>
            <button onclick="closeNotification()" style="
                background: none;
                border: none;
                font-size: 18px;
                cursor: pointer;
                color: #666;
            ">
                ✕
            </button>
        </div>
        
        <style>
        @keyframes slideIn {{
            from {{ transform: translateX(100%); opacity: 0; }}
            to {{ transform: translateX(0); opacity: 1; }}
        }}
        
        @keyframes slideOut {{
            from {{ transform: translateX(0); opacity: 1; }}
            to {{ transform: translateX(100%); opacity: 0; }}
        }}
        </style>
        
        <script>
        function closeNotification() {{
            const notification = document.getElementById('pushNotification');
            notification.style.animation = 'slideOut 0.3s ease-out forwards';
            setTimeout(() => notification.remove(), 300);
        }}
        
        // Auto close after 5 seconds
        setTimeout(closeNotification, 5000);
        </script>
        """
        
        return html