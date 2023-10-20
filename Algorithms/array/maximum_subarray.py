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