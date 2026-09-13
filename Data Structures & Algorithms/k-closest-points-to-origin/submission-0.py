class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            distance = x * x + y * y
            heapq.heappush(heap, (distance, point))

        res = []
        for i in range(k):
            distance, point = heapq.heappop(heap)
            res.append(point)
        return res