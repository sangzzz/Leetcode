class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def medians(a):
            x = len(a)
            if x % 2 == 0:
                return (a[x//2] + a[-1 + (x//2)])/2
            else:
                return (a[x//2])
        return medians(sorted(nums1 + nums2))
