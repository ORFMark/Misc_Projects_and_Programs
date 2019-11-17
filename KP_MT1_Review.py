##This is the homework for week 4, as created by Mark Burrell, and Everything Runs
import random ##imports the liabrary that allows use of random functions
import time
import sys
print("HW4_MRB_09_26_17")
Correct_Answers = 0
Incorrect_Answers = 0
questions = 0
def questionGen(info): ##A function for the creation of multiple choice questions with 4 possible option
    global Correct_Answers ##calls the program-wide variable
    global Incorrect_Answers
    global questions
    shell = sys.stdout.shell
    questions +=1
    ##begin answer list creation and randomization
    answerList=[]
    answerList.append(info[1])
    answerList.append(info[2])
    answerList.append(info[3])
    answerList.append(info[4])
    random.shuffle(answerList)
    ##end answer list
    print(info[0])
    print("A",answerList[0],"\n")
    print("B",answerList[1],"\n")
    print("C",answerList[2],"\n")
    print("D",answerList[3],"\n")
    ##Sets up the answer check lists
    if info[1] == answerList[0]:
        cAns=['A','a']
        iAns=['B','b','c','C','d','D']
    elif info[1] == answerList[1]:
        cAns=['B','b']
        iAns=['A','a','c','C','d','D']
    elif info[1] == answerList[2]:
        cAns=['C','c']
        iAns=['B','b','a','A','d','D']
    elif info[1] == answerList[3]:
        cAns=['D','d']
        iAns=['B','b','c','C','a','A']
    ##end creation of answer check lists
        ##asks the user for input and checks it against the lists, responds appropriatly
    while True:
        userAns=str(input("What is the Answer? "))
        if userAns in cAns:
            shell.write("You have chosen wisely\n", "STRING")
            Correct_Answers+=1
            break
        elif userAns in iAns:
            shell.write("You have chosen poorly\n",'COMMENT')
            Incorrect_Answers+=1
            break
        else:
            print("Not a valid Answer")
    cAns.clear()
    iAns.clear()
        ##end answer check
        ##actual quiz questions

random.shuffle(question);
qList=[]
Qnum=int(input("How many questions do you want? (enter 0 for all of them)"))
if Qnum == 0:
    qList = question
    print("Using All Questions")
elif Qnum > len(question):
         print("Your number is greater then the number of avalible questions, using all avalible.")
         qList = question
else:
    print("Generating Quiz")
    q = [];
    while len(q) < Qnum:
         n = random.randint(0, len(question)-1)
         if n in q:
             continue
         else:
             q.append(n)
    for i in q:
        qList.append(question[i])
for i in qList:
    questionGen(i)
##end quiz gen
print("Your score is",int((Correct_Answers/questions)*100), "Percent") ##Prints the score
time.sleep(1);
