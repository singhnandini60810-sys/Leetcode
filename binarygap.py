class Solution:
    def binaryGap(self, n):
        prev = -1
        max_dist = 0
        pos = 0
        
        while n > 0:
            if n & 1:
                if prev != -1:
                    max_dist = max(max_dist, pos - prev)
                prev = pos
            n >>= 1
            pos += 1
        
        return max_dist
