class Solution(object):
    def reverse(self, x):
        sign = 1
        if abs(x) > 2147483648 - 1:
            return 0

        if x < 0:
            sign = -1
            x = x * -1
        
        x = list(str(x))
        x.reverse()

        ans = ""
        for num in x:
            ans += num
        
        if abs(int(ans)) > 2147483648 - 1:
            return 0
        return int(ans) * sign
