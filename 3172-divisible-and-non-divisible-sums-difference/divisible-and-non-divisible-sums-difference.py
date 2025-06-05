class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num_1=[]
        num_2=[]
        for i in range(1,n+1):
            if i % m!=0:
                num_1.append(i)
            else:
                num_2.append(i)
        return sum(num_1)-sum(num_2)


        