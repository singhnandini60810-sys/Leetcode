class Solution:
    def minAbsDiff(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                
                values = []
                
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        values.append(grid[x][y])
                
                # REMOVE DUPLICATES (IMPORTANT FIX)
                values = sorted(set(values))
                
                # If only one distinct value → answer = 0
                if len(values) < 2:
                    ans[i][j] = 0
                    continue
                
                min_diff = float('inf')
                
                for t in range(1, len(values)):
                    min_diff = min(min_diff, values[t] - values[t-1])
                
                ans[i][j] = min_diff
        
        return ans
