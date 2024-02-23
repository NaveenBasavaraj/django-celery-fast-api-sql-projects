class TwoSum:
    def returnIndex(self,nums, target):
        numIndexDict = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numIndexDict:
                return (i, numIndexDict[diff])
            else:
                numIndexDict[num] = i
    
    def returnPairs(self, nums, target):
        pairs = set()
        numIndexDict = {}
        
        for i, num  in enumerate(nums):
            diff = target - num
            if diff in numIndexDict:
                pairs.add((i, numIndexDict[diff]))
            else:
                numIndexDict[num] = i
        return pairs

result = TwoSum().returnIndex(nums=[1, 2, 3, 4, 5], target=8)

print(result)

result = TwoSum().returnPairs(nums=[1, 2, 3, 4, 5], target=8)

print(result)


