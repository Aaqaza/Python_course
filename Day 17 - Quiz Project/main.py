from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    """Change question["question"] -> question["text"] to activate commented block of data"""
    question_answer = question["correct_answer"]
    """Change question["correct_answer"] to activate commented block of data"""
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz. You're final score was : {quiz.score}/{quiz.question_number}")
# OR
# print(f"You've complete the quiz. Your final score was {quiz.final_score}")
