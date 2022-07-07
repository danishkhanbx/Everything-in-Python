# Mapping Types — dict. A pair of braces creates an empty dictionary: {}, dictionary is a set of key: value pairs.
# Dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.
# Tuples can be used as keys if they contain only strings, numbers, or tuples;
# if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
# The main operations on a dictionary are storing a value with some key and extracting the value given in the key.
tel = {'jack': 4089, 'sape': 4139}
tel['guido'] = 4172
print(tel)

# We can delete a key:value pair with del. If you store using a key that is already in use,
# the old value associated with that key is forgotten. It is an error to extract a value using a non-existent key.
del tel['sape']
tel['irv'] = 4172
print(tel)
tel['guido'] = 4132
print(tel)

print(list(tel))  # Performing list(d) on a dictionary returns a list of all the keys used in the dictionary,
print(sorted(tel))  # in insertion order (if you want it sorted, just use sorted(d) instead).

# To check whether a single key is in the dictionary, use the "in" keyword.
print('guido' in tel)
print('jack' not in tel)

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
print(dict([('john', 9322), ('quin', 9488), ('mist', 9876)]))

# dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
x = {x: x ** 2 for x in (2, 4, 6)}
print(x)

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
print(dict(hen=877, jan=878, ken=843))

