import sys
import re

with open(sys.argv[1], 'r') as file:
    quiz = file.read()

quiz.replace(",","_").replace(";",":")
questions = filter(None,quiz.split("Question"))
qnaStr = ""

i = 0
for question in questions:
    m = re.search('[A-Z]',question)
    qnaLst = question[m.start():].split("\n")
    qnaStr = qnaStr + qnaLst[0].strip();
    answerLst = []

    j = 0
    for answer in qnaLst:
        if "Correct" in answer and len(answer) < 9:
            answerLst.append(qnaLst[j + 1])
        elif "Correct" in answer:
            answerLst.append(answer.split("Correct")[1])
        j = j + 1

    qnaStr += "," + answerLst[0].strip() + ";"
    i = i + 1

with open('qna.txt', "w") as qna:
    qna.write(qnaStr)
