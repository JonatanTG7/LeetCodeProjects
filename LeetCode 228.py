def summaryRanges(nums: list[int]) -> list[str]:

    range_list = []
    start = 0 
    end = 0
    
    for index in range(len(nums)):

        if end < len(nums) - 1 and nums[index] + 1 == nums[end + 1]:
            end += 1

        else:
            
            if start == end:
                range_list.append(f"{nums[start]}")

            if start != end:
                range_list.append(f"{nums[start]} -> {nums[end]}")

            end += 1
            start = end

    return range_list

nums = [1,2,3,4,5,6,7,8]
result = summaryRanges(nums)
print(result)