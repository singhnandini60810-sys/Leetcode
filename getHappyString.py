class Solution:
    def getHappyString(self, n, k):
        result = []

        def backtrack(current):
            if len(current) == n:
                result.append(current)
                return
            
            for ch in ['a', 'b', 'c']:
                if not current or current[-1] != ch:
                    backtrack(current + ch)

        backtrack("")

        if k <= len(result):
            return result[k-1]
        return ""
