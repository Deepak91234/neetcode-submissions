class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        grp = {}
        for i in range(len(nums)):
           grp[nums[i]] = grp.get(nums[i],0) + 1
        result = next(k for k, v in grp.items() if v > 1)
        return result
        