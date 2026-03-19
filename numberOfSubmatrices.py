class Solution:
    def numberOfSubmatrices(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        # prefix count arrays
        countX = [[0]*n for _ in range(m)]
        countY = [[0]*n for _ in range(m)]
        
        result = 0
        
        for i in range(m):
            for j in range(n):
                
                # current cell contribution
                x = 1 if grid[i][j] == 'X' else 0
                y = 1 if grid[i][j] == 'Y' else 0
                
                # build prefix
                countX[i][j] = x
                countY[i][j] = y
                
                if i > 0:
                    countX[i][j] += countX[i-1][j]
                    countY[i][j] += countY[i-1][j]
                if j > 0:
                    countX[i][j] += countX[i][j-1]
                    countY[i][j] += countY[i][j-1]
                if i > 0 and j > 0:
                    countX[i][j] -= countX[i-1][j-1]
                    countY[i][j] -= countY[i-1][j-1]
                
                # check conditions
                if countX[i][j] == countY[i][j] and countX[i][j] > 0:
                    result += 1
        
        return result
