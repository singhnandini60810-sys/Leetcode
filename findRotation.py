class Solution:
    def findRotation(self, mat, target):
        n = len(mat)
        
        for _ in range(4):
            if mat == target:
                return True
            
            # rotate 90 degree
            mat = list(zip(*mat[::-1]))
            mat = [list(row) for row in mat]
        
        return False
