class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for r in range(len(nums)+1):
            for combo in combinations(nums,r):
                res.add(combo)
        
        return [list(t)for t in res]