# if Statement
if True:
    print("Print the value")

if False:
    print("Won't print hte value")

# else Statement
r = 2 % 2
if r == 0:
    print('Even')
else:
    print('Odd')

# There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is short for ‘else if’,
# and is useful to avoid excessive indentation.
# An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.
x = int(input("Enter a value: "))
if x < 0:
    print("Negative Number")
elif x == 0:
    print("Zero")
else:
    print("Positive Number")
