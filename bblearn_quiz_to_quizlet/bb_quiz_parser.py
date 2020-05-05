import sys
import re

with open(sys.argv[1], 'r') as file:
    quiz = file.read()

quiz = quiz.replace(",","#comma#").replace(";","#semicolon#")

questions = filter(None,quiz.split("Question"))
qnaStr = ""

def addOptions(question):
    optionsStr = ""
    for k in range(1,len(question)):
        if "Selected Answer" in question[k]:
            break
        if question[k]:
            print(qnaLst[k])
            optionsStr += '\n' + question[k]
    return optionsStr

for question in questions:
    # in bblearn, the question starts with the first capital letter
    m = re.search('[A-Z]',question)
    qnaLst = question[m.start():].split("\n")

    qnaStr += qnaStr + qnaLst[0].strip();

    # sometimes part of the question is below the initial question, this adds it
    qnaStr += addOptions(qnaLst)

    answerLst = []
    j = 0
    for answer in qnaLst:
        if "Correct" in answer and len(answer) < 9:
            answerLst.append(qnaLst[j + 1])
        elif "Correct" in answer:
            answerLst.append(answer.split("Correct")[1])
        j = j + 1

    qnaStr += "," + answerLst[0].strip() + ";"

with open(sys.argv[2], "w") as qna:
    qna.write(qnaStr)
