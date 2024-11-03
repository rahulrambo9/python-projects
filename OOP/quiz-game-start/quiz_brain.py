class Quizbrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f" Q.{self.question_num}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_que(self):
        '''
        if self.question_num < len(self.question_list):
            return True
        else:
            False
        '''
             #or
        return self.question_num < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You Got it right...")
        else:
            print("Wrong Anser....!")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score:  {self.score}/{self.question_num}")    
