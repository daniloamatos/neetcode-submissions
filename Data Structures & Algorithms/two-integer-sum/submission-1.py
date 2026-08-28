class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        charlie = {}
        rest = 0
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in charlie:
                return[charlie.get(rest), i]
            charlie[nums[i]] = i
