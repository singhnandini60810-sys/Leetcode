class Solution:
    def largestSubmatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        # Step 1: build heights
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0
        
        # Step 2: process each row
        for row in matrix:
            row.sort(reverse=True)
            
            for j in range(n):
                area = row[j] * (j + 1)
                max_area = max(max_area, area)
        
        return max_area
