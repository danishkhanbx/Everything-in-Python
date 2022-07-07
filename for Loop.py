# for statement iterates over the items of any sequence (list || string), in the order that they appear in the sequence.

x = ['Jay', 16, 989892382]
for i in x:
    print(i)

for j in {'Paul', 54, 89392903}:
    print(j)

for k in range(5):
    print(k)

for v in range(11, 20, 2):  # start from 11(included) till 20(excluded) with a gap of 2
    print(v)

for d in range(20, 11, -1):  # reverse order: start from 20(included) till 11(excluded) with a gap of 2
    print(d)

words = ['cats', 'window', 'defence']
for w in words:
    print(w, len(w))

# for-else
nums = [5, 6, 9, 8, 2]
for num in nums:
    if num % 5 == 0:
        print(num)
        break;
else:
    print("Not found")
