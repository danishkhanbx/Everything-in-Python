"""
# Normal Function
def square(a):
    return a * a


result = square(5)
print(result)
"""

# Lambda Function
sq = lambda a: a * a

result = sq(5)
print(result)

add = lambda a, b: a + b  # Multiple Expression

res = add(5, 6)
print(res)
