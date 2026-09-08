class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        sorted_freq = sorted(freq, key=freq.get, reverse=True)
        return sorted_freq[:k]
sol = Solution()
nums = [1,2,2,3,3,3]
k = 2
result = sol.topKFrequent(nums,k)
print(result)        