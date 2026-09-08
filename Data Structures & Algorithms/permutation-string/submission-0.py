class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        n = len(s2)
        for i in range(n - right + 1):
            if sorted(s2[left:right]) == sorted(s1):
               return True
            else:
                left += 1
                right += 1
        return False
        