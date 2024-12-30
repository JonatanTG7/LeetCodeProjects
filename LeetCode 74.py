def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    left_index = 0
    right_index = (len(matrix[0]) * len(matrix) ) - 1

    while left_index <= right_index:
        mid = (left_index + right_index) // 2

        m_index = mid // len(matrix[0])
        n_index = mid % len(matrix[0])

        if matrix[m_index][n_index] == target:
            return True 
        
        if matrix[m_index][n_index] < target:
            left_index = mid + 1
        else:
            right_index = mid - 1
        
    return False

resulte = searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]] , 3)
print(resulte)