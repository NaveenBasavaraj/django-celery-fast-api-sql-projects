def findUnique(nums):
    result = 1
    for num in nums:
        result ^= num
    return (result)

nums = [1,2,3,4,1,2,3,4,6,9]

result = findUnique(nums)
print(result)