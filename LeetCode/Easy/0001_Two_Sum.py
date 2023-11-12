class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)-1):
            x = nums[i]
            for j in range(i+1, len(nums)):
                y = nums[j]
                if x + y == target:
                    output.append(i)
                    output.append(j)
                    return output