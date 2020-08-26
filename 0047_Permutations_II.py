class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = []

        def p(num, sol):
            if len(sol) == len(nums):
                if sol not in perm:
                    perm.append(sol)

            for i in range(0, len(num)):
                try:
                    p(num[0:i] + num[i+1:], sol + [num[i]])
                except:
                    p(num[0:i], sol + [num[i]])

        p(nums, [])
        return perm
