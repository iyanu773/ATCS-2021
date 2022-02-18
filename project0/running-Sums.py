nums = [1,1,1,1,1]
newNums = []
def runningSum(nums):
    for x in range(len(nums)):
        total = 0
        y = x
        while(y >= 0):
            total = nums[y] + total
            y = y - 1

        newNums.append(total)

    print (newNums)

runningSum(nums)



