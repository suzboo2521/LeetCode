class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def reverse(x: int) -> int:
            return int(str(x)[::-1])
        
        for x in range(num + 1):
            if x + reverse(x) == num:
                return True
        return False
