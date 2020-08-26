class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for i in nums:
            if i != val:
                c += 1
                nums[c-1] = i
        nums = nums[0:c]
        return c
