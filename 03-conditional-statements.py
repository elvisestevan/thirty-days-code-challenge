import math

def is_number_weird(n):
    if ((math.fmod(n, 2)) == 1):
        return "Weird"
    else:
        if (n >= 2 and n <= 5) or (n > 20):
            return "Not Weird"
        else:
            return "Weird"
    

if __name__ == '__main__':
    N = int(input())
    print(is_number_weird(N))
    
