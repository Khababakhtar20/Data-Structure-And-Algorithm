class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by spaces
        words = s.split()
        # Reverse each word using slicing
        reversed_words = [word[::-1] for word in words]
        # Join the reversed words back into a single string
        return " ".join(reversed_words)


        
        