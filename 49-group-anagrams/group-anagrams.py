from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for i in range(len(strs)):
            sort = "".join(sorted(strs[i]))
            if sort not in dic:
                dic[sort] = []
            dic[sort].append(strs[i])

        return list(dic.values())
