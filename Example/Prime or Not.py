from math import sqrt

n = 3
if n > 1:
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            print("Not Prime")
    else:
        print("Prime")
else:
    print("Not Prime")
