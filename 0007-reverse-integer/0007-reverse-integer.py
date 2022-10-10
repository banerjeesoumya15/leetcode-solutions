class Solution:
    def reverse(self, x: int) -> int:
        
        neg = True if x < 0 else False
        if neg:
            x = str(x)[1:]
            x = -int(x[::-1])
        else:
            x = str(x)
            x = int(x[::-1])
            
        if x < -(2**31) or x > (2**31)-1:
            return 0
        return x
        