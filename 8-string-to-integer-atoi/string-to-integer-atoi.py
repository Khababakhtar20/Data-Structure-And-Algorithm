class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        n = len(s)
        i = 0

        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0

        # Handle sign
        sign = 1
        if s[i] in ('-', '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Convert numbers
        result = 0
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            # Check for overflow before updating result
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
