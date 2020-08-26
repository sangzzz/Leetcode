class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = []
        for i in range(0, len(nums)):
            if nums[i] == target:
                ans.append(i)
                pass
        if len(ans) == 1:
            return ans[0]
        elif len(ans) == 0:
            return -1
