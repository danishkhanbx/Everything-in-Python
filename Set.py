# A set is an unordered collection with no duplicate elements. Use membership testing and eliminating duplicate entries.
# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # show that duplicates have been removed

# fast membership testing
print('orange' in basket)
print('crabgrass' in basket)

# Demonstration of set operations on unique letters from two words
print()
a = set('abracadabra')
b = set('alacazam')
print(a)      # unique letters in a
print(a - b)  # letters in a but not in b
print(a | b)  # letters in a or b or both
print(a & b)  # letters in both a and b
print(a ^ b)  # letters in a or b but not both

# set comprehensions
print()
c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)