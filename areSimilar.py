class Solution:
    def areSimilar(self, mat, k):
        m = len(mat)
        n = len(mat[0])
        
        k = k % n
        
        for i in range(m):
            if i % 2 == 0:
                shifted = mat[i][k:] + mat[i][:k]     # left shift
            else:
                shifted = mat[i][-k:] + mat[i][:-k]   # right shift
            
            if shifted != mat[i]:
                return False
        
        return True
