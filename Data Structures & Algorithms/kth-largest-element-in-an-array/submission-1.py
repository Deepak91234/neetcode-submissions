class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = 0
        nums = [-f for f in nums]
        heapq.heapify(nums)
        for i in range(k):
            s = heapq.heappop(nums)
            res = s
        return -res

