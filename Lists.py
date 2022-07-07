## Sequence Types : list, tuple, range
# List can be written as a list of comma-separated values (items) between square brackets.
# Lists might contain items of different types, but usually the items all have the same type.
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])  # indexing returns the item
print(squares[-1])
print(squares[-3:])  # slicing returns a new list
print(squares[:])  # returns a shallow copy of the list
print(squares + [36, 49, 64, 81, 100])  # concatenation

# Unlike strings, which are immutable, Lists are mutable
print()
cubes = [1, 8, 27, 65, 125]  # something's wrong here, i.e. 4^3=64
print("Wrong Cubes List:", cubes)
cubes[3] = 64
print(cubes)
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
print()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters, "of Length", len(letters))
letters[2:5] = ['C', 'D', 'E']  # replacing some values
print(letters)
letters[2:5] = []  # now removing them
print(letters)
letters[:] = []  # clearing the list by replacing all the elements with an empty list
print(letters)

# Creating lists containing other lists
print()
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

