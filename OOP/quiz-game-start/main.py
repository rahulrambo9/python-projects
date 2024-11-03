from question_model import Questions
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for que in question_data:
    que_text = que["text"]
    que_ans = que["answer"]
    que_obj = Questions(que_text, que_ans)  
    question_bank.append(que_obj)   

quiz = Quizbrain(question_bank)

while quiz.still_has_que():
    quiz.next_question()        