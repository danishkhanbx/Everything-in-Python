# Using temporary location
a = 1
b = 2
temp = a
a = b
b = temp
print(a, " ", b)

# Using XOR
a = 3  # 0011
b = 4  # 0100
a = a ^ b
b = a ^ b
a = a ^ b
print(a, " ", b)

# Using Python's rotation of two function
a = 5
b = 6
a, b = b, a
print(a, " ", b)
