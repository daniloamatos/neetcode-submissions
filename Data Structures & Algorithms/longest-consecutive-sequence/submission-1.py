class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSorted = sorted(nums)
        uniqueList = list(dict.fromkeys(numsSorted))
        sequence = 0
        best = 0
        for i, j in enumerate(uniqueList[:-1]):
            if uniqueList[i + 1 ] - j == 1 :
                sequence+=1
            else:
                sequence = 0
            best = max(best, sequence)
        return best + 1 if nums else 0
        