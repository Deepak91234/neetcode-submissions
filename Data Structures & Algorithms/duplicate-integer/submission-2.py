class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False

sol = Solution()
print ("true" if sol.hasDuplicate([1, 2, 3, 3]) else "false")