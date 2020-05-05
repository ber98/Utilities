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
    print(i)
    if m:
        print(question[m.start():])
    qnaLst = question[m.start():].split("\n")
    print("ANSWER LIST: ")
    print(qnaLst)
    qnaStr = qnaStr + qnaLst[0].strip();
    print("CORRECT ANSWER")
    answerLst = []
    j = 0
    for answer in qnaLst:
        if "Correct" in answer and len(answer) < 9:
            answerLst.append(qnaLst[j + 1])
        elif "Correct" in answer:
            answerLst.append(answer.split("Correct")[1])
        j = j + 1
    print("HELLO THERE ___________ " + answerLst[0])
    qnaStr += "," + answerLst[0].strip() + ";"
    print('\n\n')
    i = i + 1
print("FINAL STRING: " + qnaStr)
