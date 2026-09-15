class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l<r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        if nums[r] == target:
            return r
        elif nums[r] > target:
            return -1
        if r == 0:
            result = self.binarySearch(0, len(nums) - 1, nums, target)
        elif nums[0] <= target:
            r -= 1
            result = self.binarySearch(0, r, nums, target)
        else:  
            l = r
            r = len(nums) - 1
            result = self.binarySearch(l, r, nums, target)
        return result if nums[result] == target else -1

    def binarySearch(self, l, r, nums, target):
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m + 1
        return r