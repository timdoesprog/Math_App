# 06.03.2017
# ask the user math questions
# and time their answers


from questions import Add, Multiply
import datetime
import random


class Quiz:
    questions = []
    answers = []
    points = 0

    def __init__(self):
        # generate 10 random questions with numbers from 1 to 10
        ran_gen = random.randint
        for i in range(10):
            question = random.choice([Add(ran_gen(0, 10), ran_gen(0, 10)),
                                      Multiply(ran_gen(0, 10), ran_gen(0, 10))
                                      ])
            # add these questions into self.questions
            self.questions.append(question)

    def take_quiz(self):
        # log the start time
        start = datetime.datetime.now()
        # ask all of the questions
        for question in self.questions:
            self.ask(question)
        # log the end time
        end = datetime.datetime.now()
        # show summary (time and correct answers/points)
        self.summary(start, end)

    def ask(self, question):
        # log the start time
        # capture the answer
        answer = int(input("{}\n".format(question.text)))
        # check the answer
        if answer == question.answer:
            self.points += 1
        # log end time
        # if the answer is right -> True
        # else -> False
        # send back the elapsed times

    def summary(self, start, end):
        # print how many answers right/amount of questions
        print("You got {} of {} questions right!".format
              (self.points, len(self.questions)))
        # print the total time for the quiz
        delta = end - start
        print("Your total time was {} seconds!".format(delta.seconds))
