class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        def fact(i):
            if i <= 1:
                return 1
            return i*fact(i-1)

        def assign_digit(list_nums, k):
            N = len(list_nums)
            if N == 0:
                return []
            f = fact(N-1)
            if k % f == 0:
                m = (k-1)//f
                k_ = f
            else:
                m = k//f
                k_ = k % f
            if m == N-1:
                return [list_nums[m]] + assign_digit(list_nums[0:m], k_)
            else:
                return [list_nums[m]] + assign_digit(list_nums[0:m] + list_nums[m+1:], k_)
        sol = assign_digit([i for i in range(1, n+1)], k)

        x = ""
        for i in sol:
            x += str(i)
        return x
