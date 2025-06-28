class DetectSquares:

    def __init__(self):
      self.cnt = defaultdict(Counter)  

    def add(self, point: List[int]) -> None:
        x,y = point
        self.cnt[x][y] +=1
        

    def count(self, point: List[int]) -> int:
        x1 , y1 = point
        total = 0

        if x1 not in self.cnt:
            return 0

        for x2 , ys in self.cnt.items():
            if x2 == x1:
                continue
            d = x2-x1

            total += ys[y1] * self.cnt[x1][y1 + d] * ys[y1+d]
            total += ys[y1] * self.cnt[x1][y1 - d] * ys[y1-d]
        return total


        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)