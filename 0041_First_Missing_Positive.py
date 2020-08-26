class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m = 2**31-1
        T = {}
        for i in nums:
            if i > 0:
                T[i] = 1
                if i < m:
                    m = i

        if m != 1:
            return 1
        i = 2
        while True:
            if i not in T:
                return i
            i += 1
