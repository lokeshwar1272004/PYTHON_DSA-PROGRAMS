class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        d = {}
        for i in range(len(nums)):
            values = nums[i]
            difference = target - values
            if values not in d:
                d[difference] = i
            else:
                return [d[values], i]
#[5,5,6]
#10
#two sum
#10-5=5
#diff=5