def majorityElement(nums: list[int]) -> int:
    # dict_element = {}
    # for num in nums:
    #     if num in dict_element:
    #         dict_element[num] += 1
    #     else:
    #         dict_element[num] = 1

    #     if dict_element[num] > len(nums) / 2:
    #         return num

    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        
        if candidate == num:
            count +=1
        else:
            count -=1
    return candidate


nums = [2,1]
result = majorityElement(nums)
print(result)