import math

n = int(input())

def isPrime(number):
    squareRoot = int(math.sqrt(number))
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, squareRoot + 1):        
        if number % i == 0:
            return False
            break

    return True

for i in range(n):
    number = int(input())
    if isPrime(number):
        print("Prime")
    else:
        print("Not prime")
