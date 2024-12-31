def max_path_sum(matrix):
    n, m = len(matrix), len(matrix[0])  # Dimensions of the matrix

    # Create a dp matrix for calculations
    dp = [[0] * m for _ in range(n)]

    # Initialize the first cell
    dp[0][0] = matrix[0][0]
    print(f"Initialized dp[0][0] = {dp[0][0]}")

    # Fill the first row (can only come from the left)
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
        print(f"dp[0][{j}] = dp[0][{j-1}] + matrix[0][{j}] -> {dp[0][j]}")

    # Fill the first column (can only come from above)
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
        print(f"dp[{i}][0] = dp[{i-1}][0] + matrix[{i}][0] -> {dp[i][0]}")

    # Fill the rest of the dp matrix
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = matrix[i][j] + max(dp[i-1][j], dp[i][j-1])
            print(f"dp[{i}][{j}] = matrix[{i}][{j}] + max(dp[{i-1}][{j}], dp[{i}][{j-1}]) -> {dp[i][j]}")

    # The result is in the bottom-right corner of the dp matrix
    print("\nFinal dp matrix:")
    for row in dp:
        print(row)
    return dp[n-1][m-1]

# Test case
matrix = [
    [5, 3, 2, 1],
    [1, 2, 10, 1],
    [4, 3, 1, 20]
]
result = max_path_sum(matrix)
print(f"\nMax path sum: {result}")
