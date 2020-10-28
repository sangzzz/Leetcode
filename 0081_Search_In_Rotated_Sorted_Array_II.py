class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        try:
            nums.index(target)
            return True
        except:
            return False
