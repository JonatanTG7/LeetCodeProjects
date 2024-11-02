class Solution(object):
    def twoSum(self, nums, target):
        new_dict = {}

        for index,num in enumerate(nums):
            temp = target- num

            if temp in new_dict:
                return [new_dict[temp], index]
            new_dict[num]=index


nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)
print(result)

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]