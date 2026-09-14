class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rest = None
        past = {}
        for i, num in enumerate(nums):
            rest = target - num
            if rest in past:    
                return [past[rest], i]
            past[num] = i
        return [None, None]