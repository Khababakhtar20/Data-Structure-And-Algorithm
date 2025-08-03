from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i].reverse()  # Reverse each row
            for j in range(len(image[i])):
                image[i][j] = 1 - image[i][j]  # Flip the bits (0 → 1, 1 → 0)
        
        return image
