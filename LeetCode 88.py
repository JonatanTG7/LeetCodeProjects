def merge(nums1: list[int],nums2: list[int], m, n):
    index_m_n = len(nums1) - 1
    
    while n > 0 and m > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[index_m_n] = nums1[m-1]
            m -= 1
        elif nums1[m-1] < nums2[n-1]:
            nums1[index_m_n] = nums2[n-1]
            n -= 1
        else:
            nums1[index_m_n] = nums1[m-1]
            m -= 1
        index_m_n -= 1

    while n > 0:
        nums1[index_m_n] = nums2[n-1]
        n -= 1
        index_m_n -= 1

nums1 = [1,2,2,2,3,3,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0]
m = 9
nums2 = [2,5,7,8,8,8,8,8,8,8,9,9,9]
n = 13

merge(nums1, nums2, m, n)