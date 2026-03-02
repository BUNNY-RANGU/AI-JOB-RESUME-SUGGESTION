import random

class InterviewSimulator:
    """AI Interview Practice"""
    
    def __init__(self):
        self.questions_db = {
            'python': [
                "Explain Python decorators with example",
                "Difference between list and tuple",
                "What are Python generators?",
                "Explain GIL in Python"
            ],
            'dsa': [
                "Explain binary search algorithm",
                "What is time complexity of quicksort?",
                "Difference between BFS and DFS",
                "What is a hash table?"
            ],
            'web': [
                "Explain REST API principles",
                "Difference between GET and POST",
                "What is CORS?",
                "Explain React lifecycle methods"
            ],
            'behavioral': [
                "Tell me about yourself",
                "Why should we hire you?",
                "Describe a challenging project",
                "Where do you see yourself in 5 years?"
            ]
        }
    
    def get_questions(self, topics, num_questions=5):
        """Get interview questions"""
        questions = []
        for topic in topics:
            if topic in self.questions_db:
                questions.extend(self.questions_db[topic])
        
        random.shuffle(questions)
        return questions[:num_questions]
    
    def evaluate_answer(self, question, user_answer):
        """Simple answer evaluation"""
        # In reality, use AI for evaluation
        keywords = {
            'python decorators': ['function', 'wrapper', '@symbol', 'modify'],
            'rest api': ['stateless', 'http', 'get/post', 'json'],
            'binary search': ['sorted', 'log n', 'divide', 'conquer']
        }
        
        score = 50  # Base score
        
        for keyword, required_words in keywords.items():
            if keyword in question.lower():
                matches = sum(1 for word in required_words if word in user_answer.lower())
                score += matches * 10
        
        return {
            'score': min(score, 100),
            'feedback': self.generate_feedback(score),
            'model_answer': self.get_model_answer(question)
        }
    
    def generate_feedback(self, score):
        """Generate feedback based on score"""
        if score >= 80:
            return "Excellent answer! Clear and comprehensive."
        elif score >= 60:
            return "Good answer. Could add more technical details."
        else:
            return "Needs improvement. Focus on key concepts."
    
    def get_model_answer(self, question):
        """Get model answer"""
        answers = {
            "Explain Python decorators": "Decorators are functions that modify other functions...",
            "Difference between list and tuple": "Lists are mutable, tuples are immutable...",
            "What is REST API": "REST stands for Representational State Transfer..."
        }
        
        for key in answers:
            if key.lower() in question.lower():
                return answers[key]
        
        return "A good answer should cover key concepts clearly."

# Test
if __name__ == "__main__":
    simulator = InterviewSimulator()
    questions = simulator.get_questions(['python', 'behavioral'], 3)
    print("Sample Questions:", questions)