class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge=sorted(nums1+nums2)
        l=len(merge)
        if l%2==0:return (merge[l//2]+merge[l//2-1])/2
        return merge[l//2]
        