def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    answer = []

    for i in range(n):
        if nums[i]>0:
            break
        elif i > 0 and nums[i] == nums[i-1]:
            continue

        left , right = i+1, n-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum == 0:
                answer.append([nums[i], nums[left] , nums[right]])

                left , right = left +1 , right -1
                while left < right and nums[left] == nums[left-1]:
                    left = left+1
                while left < right and nums[right] == nums[right+1]:
                    right = right-1
            
            elif sum > 0:
                right = right -1
            else:
                left = left+1

    return answer

nums = [-2,0,0,2,2]
print(threeSum(nums))
