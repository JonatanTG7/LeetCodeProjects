from collections import defaultdict
class Solution:
    def top_frequent(self,nums:list[int],k: int) -> list[int]:
        
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] +=1
            else:
                freq_dict[num] =1

        freq_list = list(freq_dict.items())

        freq_list_sorted = sorted(freq_list, key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            num , _ = freq_list_sorted[i]
            result.append(num)
        return result

solution = Solution()
list_of_k_freq=solution.top_frequent([3,1,1,2,2,3,1,1,3,5,1,3] , 2)
print(list_of_k_freq)


