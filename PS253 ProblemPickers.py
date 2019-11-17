#Problem Selector for PS250 to aid in studying
#Based on the MA225 problem picker written by Mark Burrell 10/27/2018
#Last updated 3/02/2019 and contains up to chapters 21-26
import random;
print("MRB12_1_2018")
def probList(maxProblem):
    l = [];
    for i in range(1,maxProblem,2):
        l.append(i);
    return l
problemDict = {
    "21" : 99,
    "22": 62,
    "23": 86,
    "24": 72,
    "25": 82,
    "26": 88
    }
for i in problemDict:
    problemDict[i] = probList(problemDict[i]);
focusLow = input("What is the lowest Chapter you want to focus on: ")
focusHigh = input("What is the highest Chapter you want to focus on: ")

while True:
    lowerFocus = list(problemDict.keys()).index(focusLow)
    upperFocus = list(problemDict.keys()).index(focusHigh)
##    c = random.randint(1,4);
##    if c%4 == 0:
##        key = list(problemDict.keys())[random.randint(0,len(problemDict)-1)]
##        prob = problemDict[key][random.randint(0,len(problemDict[key])-1)]
##    else:
##        key = list(problemDict.keys())[random.randint(lowerFocus,upperFocus)]
##        prob = problemDict[key][random.randint(0,len(problemDict[key])-1)]
    key = list(problemDict.keys())[random.randint(lowerFocus,upperFocus)]
    prob = problemDict[key][random.randint(0,len(problemDict[key])-1)]
    print("Do problem %d in section "%prob + key)
    correct = input("Did you get it right? (Y/N): ")
    if correct == "Y":
        problemDict[key].remove(prob)
        print("removeing value from possible questions")
        if len(problemDict[key]) == 0:
            print("Congrats, you finished all the problems in this section!")
            del problemDict[key]
    else:
        print("too bad, it will stay in the possible problems")
    if len(problemDict) == 0: 
        print("Out of Problems");
        break;
