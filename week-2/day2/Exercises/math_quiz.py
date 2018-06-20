from math_questions import *
import random
import datetime

class TheQuiz:
    options = [Add, Divide, Multiply]
    amount_questions = 3
    questions = []
    user_answers = []
    correct_answers = 0

    def __init__(self):
        for i in range(self.amount_questions):
            num1 = random.randint(0, 10)
            num2 = random.randint(0, 10)
            self.questions.append(random.choice(self.options)(num1, num2))  # questions[random.randint(0,2)]

    def start(self):
        for i, question in enumerate(self.questions):
            print(f'{question.text}')
            user_answer = float(input('Enter your answer: '))
            self.user_answers.append(user_answer)
            if user_answer == float(question.answer):
                self.correct_answers += 1
        print(f'You answered: {self.correct_answers} correctly!')
        for i, question in enumerate(self.questions):
            print(f'The question was: {question.text} - Your answer: {self.user_answers[i]} '
                  f'- Correct answer: {question.answer}')

quiz = TheQuiz()
quiz.start()
# print(quiz.get_numbers())