class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        index_up = 0
        index_down = len(numbers)-1
        while True:
            if numbers[index_up] + numbers[index_down] < target:
                index_up += 1
            elif numbers[index_up] + numbers[index_down] > target:
                index_down -= 1
            else:
                return [index_up+1,index_down+1]

solution = Solution()
resulte = solution.twoSum([2,7,11,15] , 22)
print(resulte)