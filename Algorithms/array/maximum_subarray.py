# maximum sum subarray

class MaxSubarray:
    def maxSumSubArray(self, nums):
        currSum = nums[0]
        maxSum = 0
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum +=  num
            maxSum = max(maxSum, currSum)
        return maxSum
    
    # def maxSumSubArray(self, nums):
    #     currSum = nums[0]
    #     maxSum = 0
    #     for r in range(1, len(nums)):
    #         if currSum < 0:
    #             currSum = 0
    #         currSum +=  nums[r]
    #         maxSum = max(maxSum, currSum)
    #     return maxSum
    
    def maxProductSubArray(self, nums):
        res = max(nums)
        curMin, curMax = 1,1
        for n in nums:
            tmp = curMax * n
            curMax = max(n*curMax, n* curMin, n)
            curMin = min(tmp,  n*curMin, n)
            res = max(res, curMax)
        return res