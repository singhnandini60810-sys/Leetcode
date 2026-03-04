class Solution:
    def numSteps(self, s):
        steps = 0
        carry = 0
        
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry
            
            if bit % 2 == 0:
                steps += 1
            else:
                steps += 2
                carry = 1
        
        return steps + carry
