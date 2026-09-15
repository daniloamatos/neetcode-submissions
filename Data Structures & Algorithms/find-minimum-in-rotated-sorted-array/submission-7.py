class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = r//2
        minimum = None
        if r <= 2:
            return min(nums[l], nums[r], nums[m])
        while l < r:
            minimum = min(nums[l], nums[r], nums[m])
            if nums[m] > nums[r]:
                l = m + 1
                m = (l + r) // 2
            else:
                r = m
                m = (l + r) // 2
        return minimum