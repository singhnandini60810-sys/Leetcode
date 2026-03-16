class Solution:
    def getBiggestThree(self, grid):
        m = len(grid)
        n = len(grid[0])
        sums = set()

        for i in range(m):
            for j in range(n):

                # single cell rhombus
                sums.add(grid[i][j])

                size = 1
                while True:
                    if i-size < 0 or i+size >= m or j-size < 0 or j+size >= n:
                        break

                    total = 0

                    # top -> right
                    x, y = i-size, j
                    for d in range(size):
                        total += grid[x+d][y+d]

                    # right -> bottom
                    x, y = i, j+size
                    for d in range(size):
                        total += grid[x+d][y-d]

                    # bottom -> left
                    x, y = i+size, j
                    for d in range(size):
                        total += grid[x-d][y-d]

                    # left -> top
                    x, y = i, j-size
                    for d in range(size):
                        total += grid[x-d][y+d]

                    sums.add(total)
                    size += 1

        return sorted(sums, reverse=True)[:3]
