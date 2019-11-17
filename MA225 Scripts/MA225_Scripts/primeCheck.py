import os.path
def prime(n, primeList):
    if (n % 2 == 0 and n != 2):
        return False
    maxFactor = int((n ** (1/2)) + 2)
    if(len(primeList) == 0):
        for i in range (3, maxFactor,2):
            if (n % i == 0):
                return False;
    else:
        for i in range(1, len(primeList)):
            k = primeList[i]
            if n % k == 0 and k < maxFactor:
                return False;
    return True
primeList = []
try:
    f = open('primeList.txt', 'r')
    for i in f.readlines():
        primeList.insert(0,i)
    f.close()
    for i in range(0,len(primeList)):
        primeList[i] = int(primeList[i])
    p = primeList[len(primeList)-1]
except IOError:
    p = 0;
print("Starting prime calc")
length = len(primeList)
while length < 200:
    if (prime(p, primeList)):
        primeList.append(p)
        length += 1
    p += 1
f = open("primeList.txt", "w")
print("starting writeout")
print("[", end = '')
for j in range(len(primeList)-1, -1, -1):
    f.write(str(primeList[j])+'\n')
    print(str(primeList[j]) + ', ', end = '');
f.close()
print('Done!')
