# input is a string by default. So we take might take any data type as input but it asa String.
x = input("Enter 1st String: ")
y = input("Enter 2st Stringr: ")
z = x + y
print(z)

# input in int format
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2st Number: "))
c = a + b
print(z)

# input in char format
ch = input("Enter the character: ")  # or input("Enter the character: ")[0]
print(ch[0])  # or print(ch)

# input an expression
res = eval(input('Enter the expression: '))
print(res)
