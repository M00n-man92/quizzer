from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import Extriemist
from hewasreallyfunny import Percentage
import requests




question_bank = []
personalyy=Percentage
milllions=personalyy.homosiderate()
for question in milllions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
ui=Extriemist(quiz)
ui.kindov()

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
