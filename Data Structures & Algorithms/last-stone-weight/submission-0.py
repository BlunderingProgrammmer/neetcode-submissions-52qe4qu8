class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #since py does not have  max heap we are going to simulate a max heap using a min heap
        #so get the negative
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones,first - second)#first -second give value in neg need in heap
        stones.append(0)
        return abs(stones[0])