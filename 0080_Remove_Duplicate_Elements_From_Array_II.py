class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        T = {}
        for i in nums:
            try:
                T[i] += 1
            except:
                T[i] = 1
        j = 0
        for i in T:
            if T[i] >= 2:
                nums[j], nums[j+1] = i, i
                j += 2
            else:
                nums[j] = i
                j += 1

        return j
