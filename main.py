from quiz_brain import QuizBrain
from data import get_question_data

quiz_brain = QuizBrain(get_question_data())

score = 0
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
