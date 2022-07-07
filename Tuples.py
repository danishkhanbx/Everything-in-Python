## Sequence Types : list, tuple, range
# Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking.
# A tuple consists of a number of values separated by commas.
t = (12, 56, 87, 97, 88)
print(t[0])

# Tuples may be nested:
print()
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
#t[0] = 8888    # throws an error

# But they can contain mutable objects:
print()
a = [1, 2, 3]
b = [3, 2, 1]
v = (a, b)  # tuples containing mutable objects, such as lists.
print(v)
a[0] = 4
b[0] = 5
print(v)

# Tuple packing and unpacking:
print()
p = 12345, 54321, 'hello!'  # packing
x, y, z = p                 # unpacking
print(x)
print(y)
print(z)