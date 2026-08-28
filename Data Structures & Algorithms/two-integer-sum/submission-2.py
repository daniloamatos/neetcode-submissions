class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        charlie = {}
        for i, n in enumerate(nums):
            rest = target - n
            if rest in charlie:
                return[charlie[rest], i]
            charlie[n] = i
