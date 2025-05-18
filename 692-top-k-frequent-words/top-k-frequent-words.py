class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for i in words:
            if i not in dic:
                dic[i]=1
            else:
                dic[i] += 1

        result =sorted(dic,key=lambda x:(-dic[x],x))
        return result[:k]

        