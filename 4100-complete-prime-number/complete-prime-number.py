class Solution:
    def completePrime(self, num: int) -> bool:
        def isPrime(x: int) -> bool:
            if x < 2:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True

        s = str(num)
        n = len(s)

        # Check all prefixes
        for i in range(1, n + 1):
            if not isPrime(int(s[:i])):
                return False

        # Check all suffixes
        for i in range(n):
            if not isPrime(int(s[i:])):
                return False

        return True
