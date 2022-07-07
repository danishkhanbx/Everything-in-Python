d = 10  # Let d be the number of characters in the input set


def search(pattern, text, q):
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    for i in range(m-1):  # i=0,1
        h = (h*d) % q     # i=0 h=1*10%13=10, i=1 h=10*10%13=9

    # Calculate hash value for pattern and text
    for i in range(m):  # i=0,1,2
        p = (d*p + ord(pattern[i])) % q  # i=0 p=10*0+67%13=2 t=10*0+65%13=0, i=1 p=10*2+68%13=10 t=10*0+66%13=1,
        t = (d*t + ord(text[i])) % q   # i=2 p=10*10+68%13=12 t=10*1+67%13=12

    # Find the match
    for i in range(n-m+1):  # i=0,1,2,3,4,5,6,7
        if p == t:
            for j in range(m):  # j=0,1,2 now comparing text and pattern character by character
                if text[i+j] != pattern[j]:  # if even one of them dosent match
                    break

            j += 1  # when all charcaters matched perfectly j will be 2, means we have a match
            if j == m:  # after adding 1 to j, if j matches m means we have found patter at position i+1 and index i
                print("Pattern is found at position: " + str(i+1))

        if i < n-m:  # when current index is less than last position 8(index=7) to be checked
            t = (d * (t - ord(text[i]) * h) + ord(text[i+m])) % q  # sliding window adding a new char and removing the first char
            #   10 * (12 - ord(i=0(A)) * 9) + ord(i+m=3(C)) % 13 = (10 ( 12 - 65 * 9) + 67) % 13 = 5
            if t < 0:  # if we get t in minus add the prime number to it
                t = t+q


text = "ABCCDDAEFG"
pattern = "CDD"
q = 13
search(pattern, text, q)