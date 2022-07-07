# # # #
# # # #
# # # #
# # # #
for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()

#
# #
# # #
# # # #
for i in range(4):
    for j in range(i + 1):
        print("# ", end="")
    print()

# # # #
# # #
# #
#
for i in range(4):
    for j in range(4 - i):
        print("# ", end="")
    print()

      #
    # #
  # # #
# # # #
for i in range(4):
    for j in range(4 - i - 1):
        print("  ", end="")
    for k in range(i + 1):
        print("# ", end="")
    print()

# # # #
# # #
# #
#
for i in range(4):
    for j in range(i):
        print("  ", end="")
    for k in range(4 - i):
        print("# ", end="")
    print()

      #
    # # #
  # # # # #
# # # # # # #
  # # # # #
    # # #
      #
n = 4
for i in range(n):                                 # range i start's from line 50 end at 53
    print("  " * (n - i - 1), "# " * (2 * i + 1))  # 4-0-1=3 times space + 2*0+1=1 time print #
for j in range(n - 1, 0, -1):                      # from n=3,2,1
    print("  " * (n - j), "# " * (2 * j - 1))      # 3-3=0 times space + 2*3-1=5 time print #
