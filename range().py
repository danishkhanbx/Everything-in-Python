# When we need to iterate over a sequence of num, the built-in function range() is used.
# It generates arithmetic progressions:
for i in range(5):
    print(i)

# range can also start at another number, or to specify a different increment (even negative; called as ‘step’):
print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))

# To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# function that takes an iterable is sum():
print(sum(range(4)))
