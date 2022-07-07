def fib(n):
    a, b = 0, 1
    count = 0

    if n <= 0:
        print("Enter a valid number!")
    elif n == 1:
        print(b)
    else:
        print("Fibonacci Sequence:")
        while count < n:
            print(a)
            c = a + b
            a = b
            b = c
            count += 1


terms = int(input("Enter how term number should we continue executing: "))
fib(terms)
