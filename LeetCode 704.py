class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start_index = 0
        end_index = len(nums) - 1

        while start_index <= end_index:
            mid = (start_index+end_index)//2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                start_index = mid + 1
            else:
                end_index = mid - 1
            


        return -1

                           
solution = Solution()
print(solution.search([-1,0,3,5,9,12], 12))