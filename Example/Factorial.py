# Using loop
def fact(n):
    f = 1
    for i in range(1, n + 1):  # we from 1 because 0!=1 and end at n+1(excluded) so n is get included
        f = f * i

    return f


x = int(input("Enter the number whose factorial you want: "))
result = fact(x)
print(result)


# Using recursion
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)


y = int(input("Enter the number whose factorial you want: "))
res = fact(y)
print(res)
