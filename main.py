from quiz_brain import QuizBrain
from data import get_question_data
from ui import QuizInterface

questions = get_question_data()

quiz_brain = QuizBrain(questions)
quiz_ui = QuizInterface(quiz_brain)

