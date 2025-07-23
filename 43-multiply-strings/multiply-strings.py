class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def toDigit(num: str) -> int:
            digit = 0
            for c in num:
                digit = digit * 10 + (ord(c) - ord('0'))
            return digit

        return str(toDigit(num1) * toDigit(num2))
