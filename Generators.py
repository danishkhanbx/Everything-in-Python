# Generator will give us iterators. Generator(yield) fetch values from iterator one by one.
# When we want to work one value at a time we use generator.
def TopTen():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = TopTen()
for i in values:
    print(i)


def Ten():
    yield 1
    yield 2
    yield 3
    yield 4


value = Ten()
for j in value:
    print(j)
