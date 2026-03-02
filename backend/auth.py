import hashlib
import secrets
from database import CareerDatabase

class SimpleAuth:
    """Simple authentication system"""
    
    def __init__(self):
        self.db = CareerDatabase()
    
    def register_user(self, email, password):
        """Register new user"""
        # Hash password
        salt = secrets.token_hex(8)
        hashed_password = self.hash_password(password, salt)
        
        # Store in database (simplified)
        return True
    
    def hash_password(self, password, salt):
        """Hash password with salt"""
        return hashlib.sha256((password + salt).encode()).hexdigest()
    
    def login(self, email, password):
        """Login user"""
        # Simplified for now
        return True
    
    def get_user_profile(self, email):
        """Get user profile"""
        # Return sample data
        return {
            'email': email,
            'name': 'Student User',
            'college': 'Your College',
            'year': '2nd Year',
            'avatar': '👨‍🎓'
        }