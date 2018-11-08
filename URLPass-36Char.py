import random
def wordFinder(string):
    """Takes a string and returns the number of times a word is repeated"""
    #begin init of function variables
    stringLower=string.lower()
    stringList=list(stringLower)
    stringList.insert(0,' ')
    stringList.append(' ')
    spaceList=[]
    wordList=[]
    charList=[]
    repeat=0
   #print(stringList)
    #end variable create
    for m in range (0, len(stringList)): #finds and notes all the spaces
        if stringList[m]==' ':
            spaceList.append(m)
    t=len(spaceList)
  #  print(t,spaceList)
    for i in range(0,t):
        start=spaceList[0] ##uses the spaces to find words and add them to a list
        if len(spaceList) != 1:
            end=spaceList[1]
        else:
            end=None
        charList=stringList[start+1:end]
     #   print(charList)
        for m in charList: ##removes non alpha-numeric characters
            if m.isalpha() == False:
                charList.remove(m)
            #    print("removing non-alphaCharacter")
        spaceList.pop(0)
        wordList.append("".join(charList))
    return wordList
f=open("WordList.txt","r")
wordList=f.readlines()
passseed=input("What is the URL of the website?")
usr=input("What is your username? ")
PassType=input("Would you like a passphrase(P) or a random string(R)? ")
usrseed=input(("What is the part of the seed you want to enter? (Please use a number that you will remember)"))
usrseed=int(usrseed)
passseed=list(passseed)+list(usr)
key=len(passseed)+ usrseed
random.seed(key)
random.shuffle(passseed)
pswd=[]
alphaList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#',"$","%","^","&","*","(",")",'-','_','=','+','?','.','1','2','3','4','5','6','7','8','9','0','!','@','#',"$","%","^","&","*","(",")",'-','_','=','+','?','.']
deltaList=alphaList.copy()
random.shuffle(alphaList)
if PassType=="R" or PassType=="r":
    while True:
        if len(passseed)<36:
            passseed.append(alphaList[random.randint(0,len(alphaList)-1)])
        else:
            break
    while True:
        random.shuffle(passseed)
        random.shuffle(deltaList)
        for i in range(0,len(passseed)):
            for j in range(0, len(alphaList)):
                if passseed[i]==alphaList[j]:
                    pswd.append(deltaList[j])
                    break
        if (any(c.islower() for c in pswd) and any(c.isupper() for c in pswd) and sum(c.isdigit() for c in pswd) > 2):
            break
    random.shuffle(pswd)
    pswd=pswd[0:36]
    pswd="".join(pswd)
    print("Your password is \n"+pswd)
elif PassType=="P" or PassType=="p":
    while len(pswd)<=5:
        line=wordList[random.randint(0,len(wordList)-1)]
        word=wordFinder(line)
        word=word[random.randint(0,len(word)-1)]
        for i in pswd:
            if i==word:
                break
        word=list(word)
        if len(word) >0:
            word[0]=word[0].upper()
        else:
            continue
        word=''.join(word)
        pswd.append(word)
    pswd="".join(pswd)
    print("Your password is \n"+pswd)
else:
    print("Please use P,p,R,or R when seleceting password type")
input("Press enter when you are done")
