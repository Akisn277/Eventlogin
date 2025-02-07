import random

# Sample question bank
question_bank = [
    {"subject": "Math", "topic": "Algebra", "difficulty": "Easy", "question": "Solve x+3=5"},
    {"subject": "Math", "topic": "Geometry", "difficulty": "Medium", "question": "Find the area of a circle with radius 5."},
    {"subject": "Science", "topic": "Physics", "difficulty": "Easy", "question": "Define Newton's second law."},
]

def generate_question_paper(subject, topics, difficulty, num_questions):
    filtered_questions = [
        q for q in question_bank
        if q["subject"] == subject and q["topic"] in topics and q["difficulty"] == difficulty
    ]
    return random.sample(filtered_questions, min(num_questions, len(filtered_questions)))

# Example usage
subject = "Math"
topics = ["Algebra", "Geometry"]
difficulty = "Easy"
num_questions = 2

question_paper = generate_question_paper(subject, topics, difficulty, num_questions)
for i, q in enumerate(question_paper, 1):
    print(f"{i}. {q['question']}")
