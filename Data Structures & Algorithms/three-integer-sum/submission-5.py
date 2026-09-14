class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        j, k = None, None
        missing = None
        pairs = set()
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:    
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    pairs.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j+=1
                if total < 0:
                    j+=1
                elif total > 0:
                    k-=1
        return [list(pair) for pair in pairs]
