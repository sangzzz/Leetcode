class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 0
        prev = None
        for i in nums:
            if i != prev:
                c += 1
                nums[c-1] = i
            prev = i
        return c
