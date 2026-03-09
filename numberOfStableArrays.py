class Solution:
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10**9 + 7
        memo = {}

        def dp(z, o, last, count):
            if z == 0 and o == 0:
                return 1

            key = (z, o, last, count)
            if key in memo:
                return memo[key]

            res = 0

            if z > 0:
                if last == 0:
                    if count < limit:
                        res += dp(z-1, o, 0, count+1)
                else:
                    res += dp(z-1, o, 0, 1)

            if o > 0:
                if last == 1:
                    if count < limit:
                        res += dp(z, o-1, 1, count+1)
                else:
                    res += dp(z, o-1, 1, 1)

            memo[key] = res % MOD
            return memo[key]

        ans = 0
        if zero > 0:
            ans += dp(zero-1, one, 0, 1)
        if one > 0:
            ans += dp(zero, one-1, 1, 1)

        return ans % MOD
