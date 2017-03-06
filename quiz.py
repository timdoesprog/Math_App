# 06.03.2017
# ask the user math questions
# and time their answers


from questions import Add, Multiply
import datetime


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        # generate 10 random questions with numbers from 1 to 10
        # add these questions into self.questions

    def take_quiz(self):
        # log the start time
        # ask all of the questions
        # log if they got the question right
        # log the end time
        # show summary (time and correct answers/points)

    def ask(self, question):
        # log the start time
        # capture the answer
        # check the answer
        # log end time
        # if the answer is right -> True
        # else -> False
        # send back the elapsed times

    def summary(self):
        # print how many answers right/amount of questions
        # print the total time for the quiz
