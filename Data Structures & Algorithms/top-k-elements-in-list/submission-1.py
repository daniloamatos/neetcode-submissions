class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for n in nums:
            if n in numbers:
                numbers[n] += 1
            else:
                numbers[n] = 1
        
        return sorted(numbers, key=numbers.get, reverse=True)[:k]
