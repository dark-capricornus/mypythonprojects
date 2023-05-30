import math

num = int(input())

if num <=1:
    print ("Not prime Number")
else:
    is_prime = True
    for i in range(2,int(math.sqrt(num)) + 1):
        if num %i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
            
