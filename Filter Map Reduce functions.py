from functools import reduce

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# filter
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

# map
double = list(map(lambda n: n * n, evens))
print(double)

# reduce
sum = reduce(lambda a, b: a + b, double)
print(sum)
