class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict_nums = {}
        
        for i in range(len(nums)):
            key = f"{nums[i]}"
            if key not in dict_nums:
                dict_nums[key] = 1
            else:
                return True
        return False

# Create an instance of the Solution class
solution_instance = Solution()

# Call the method with the nums argument
nums = [1, 2, 3, 1]  # Example list
result = solution_instance.containsDuplicate(nums)
print(result)
