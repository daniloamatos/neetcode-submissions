class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maximum = 0
        while l < r:
            minimum = min(heights[l], heights[r])
            curr = (r - l) * minimum
            if curr >= maximum:
                maximum = curr
            if heights[l] == minimum:
                l+=1
            else:
                r-=1
        return maximum
