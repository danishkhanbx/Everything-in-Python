# The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
# iterables	can be built-in iterables (like: list, string, dict), or user-defined iterables
# The zip() function returns an iterator of tuples based on the iterable objects.
# If we do not pass any parameter, zip() returns an empty iterator.
# If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
# If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements from all the
# iterables.

name = ('Nash', 'Mars', 'Khan')
company = ('Microsoft', 'Google', 'Apple')

zipped = list(zip(name, company))
print(zipped)
