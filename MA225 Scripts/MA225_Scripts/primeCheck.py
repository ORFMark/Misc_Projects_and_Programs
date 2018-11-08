def prime(n):
    if (n % 2 == 0):
        return False
    for i in range (3, int(n**(1/2))+2,2):
        if (n % i == 0):
            return False;
    return True
p = 0;
while True:
    if (prime(p)):
        print(p)
    p += 1;
