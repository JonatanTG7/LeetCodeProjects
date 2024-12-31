def searchInsert(nums: list[int], target: int) -> int:
    if target < nums[0]:
        return 0
    
    if target > nums[len(nums)-1]:
        return len(nums)
    
    left = 0
    right = len(nums) - 1

    while left <= right:
        print(left)
        mid = (left+right)//2
    
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left
            


nums = [2,5,7,8,9,14,15,16]
target = 11

result = searchInsert(nums,target)
print(result)

