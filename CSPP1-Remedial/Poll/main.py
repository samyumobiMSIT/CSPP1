# import Quiz, participant, Question

class Quiz:
    questions = []

    def __init__(self):
        pass

    def addQuestion(self, Question):
        self.questions.append(Question)

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

    def getText(self):
        return self.question

    def commonSelectedOption(self):
        vote = max(self.optionVotes.values())
        for optionVote in self.optionVotes:
            if self.optionVotes[optionVote] == vote:
                return optionVote


class Participant:

    def __init__(self,name, question_number, option):
        self.name = name
        self.question_number = question_number
        self.option = option

    def participant(self):
       pass

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
          line = input().split()
          q = int(line[0])
          p = Participant(name, q - 1, line[1])
          question = quiz.getQuestion(q - 1)

          question.setOptionVotes(line[1])
    for i in range(q1):
        print("Highest number of votes for question : " + quiz.getQuestion(i).getText()
                           + " : " + quiz.getQuestion(i).commonSelectedOption())


if __name__ == '__main__':
    main()
