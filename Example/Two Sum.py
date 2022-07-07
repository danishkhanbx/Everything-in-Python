nums = [2, 7, 11, 15]
target = 9
# When i=0 and j=1 2+7, 2+11, 2+15 will be calculated
# then i=1 and j=2, j!=0 because no need to calculate i=1 and j=0 i.e. 7+2  it will be the same as i=0 and j=1
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)
