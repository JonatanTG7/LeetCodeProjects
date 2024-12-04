class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_pro = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                print(f"i: {i} , j: {j}")
                if prices[j]-prices[i] > max_pro:
                    max_pro = prices[j]-prices[i]
        return max_pro


solution = Solution()
resulte = solution.maxProfit([1,2])
print(resulte)