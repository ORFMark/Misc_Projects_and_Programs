#Problem Selector for MA225 to aid in studying
#written by Mark Burrell 10/27/2018
#Last updated 12/01/2018 and contains up to chapter 8.3
import random;
print("MRB12_1_2018")
def probList(maxProblem):
    l = [];
    for i in range(1,maxProblem,2):
        l.append(i);
    return l
problemDict = {
    "1.1": 37,
    "1.2": 51,
    "1.3": 39,
    "1.4": 47,
    "2.1": 39,
    "2.2": 37,
    "2.3": 33,
    "2.4": 39,
    "3.1": 37,
    "3.2": 33,
    "3.3": 25,
    "3.4": 41,
    "3.5": 39,
    "4.1": 41,
    "4.2": 37,
    "4.3": 33,
    "4.4": 37,
    "4.5": 29,
    "4.7": 37,
    "4.8": 22,
    "5.1": 44,
    "5.2": 49,
    "5.3": 29, 
    "6.1": 41,
    "7.1": 33,
    "7.3": 37,
    "7.5": 25,
    "8.1": 33,
    "8.2": 25,
    "8.3": 25
    }
for i in problemDict:
    problemDict[i] = probList(problemDict[i]);
focusLow = input("What is the lowest section you want to focus on: ")
focusHigh = input("What is the highest section you want to focus on: ")

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
