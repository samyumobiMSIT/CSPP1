# import Quiz, participant, Question

class Quiz:
    questions = []

    def __init__(self):
        pass

    def addQuestion(self, question):
        self.questions.append(question)

    def getQuestion(self, i):
        return self.questions[i]



class Question:
    l = []
    def __init__(self,question, options):
        self.question=question
        self.options = options
        self.optionVotes = {}
        for o in options:
            self.optionVotes[o] = 0
        self.l.append(self.optionVotes)

    def setOptionVotes(self,option):
        self.optionVotes[option] +=1

    def getText(self,question):
        return self.question

    def commonSelectedOption(self):
        vote = max(self.optionVotes.values())
        for optionVote in self.optionVotes:
            if self.optionVotes[optionVote] == vote:
                return optionVote


class Participant():
     def _init_(self, name, question_number, option):

        self.name = name
        self.question_number = question_number
        self.option = option


def main():
    quiz = Quiz()
    q1 = int(input())
    for i in range(q1):
        q1s = input()
        options = []
        for i in range(4):
          options.append(input())
        a = Question(q1s,options)
        quiz.addQuestion(a)
    participants = int(input())
    for i in range(participants):
        name = input()
        for i in range(q1):
          lines = input().split()
          q = int(lines[0])
          p = Participant(name, q-1,lines[1])
          question = quiz.getQuestion(q-1)
          question.setOptionVotes(lines[1])

    for i in range(q1):
        print("Highest number of votes for question : " + quiz.getQuestion(i).getText()
                           + " : " + quiz.getQuestion(i).commonSelectedOption())


if __name__ == '__main__':
    main()
