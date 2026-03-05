class Solution:
    def minOperations(self, s):
        change_start0 = 0
        change_start1 = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    change_start0 += 1
                if s[i] != '1':
                    change_start1 += 1
            else:
                if s[i] != '1':
                    change_start0 += 1
                if s[i] != '0':
                    change_start1 += 1

        return min(change_start0, change_start1)
