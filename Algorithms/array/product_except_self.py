# array  = [2, 1, 3, 4]
# result = [12,24,8,6] 
# return a product of array except self
# you cannot use division (easiest solution is multiply everything and divide by self)

def productArray(nums):
    result = [1] * len(nums)
    for i in range(1,len(nums)):
        result[i] = result[i-1] * nums[i-1]
        print(f"{result[i-1]} * {nums[i-1]} --> {result}")

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        print(f"{result[i]} * {postfix} --> {result}")
        result[i] *= postfix
        postfix *= nums[i]
    return result

def productExceptSelf(nums):
    res = [1] * (len(nums))

    for i in range(1, len(nums)):
        res[i] = res[i-1] * nums[i-1]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


result = productArray([2,1,3,4])
print(result)
result = productExceptSelf([2,1,3,4])
print(result)