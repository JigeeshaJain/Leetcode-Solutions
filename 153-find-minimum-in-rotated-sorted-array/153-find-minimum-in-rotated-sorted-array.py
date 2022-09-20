class Solution:
    def findMin(self, nums: List[int]) -> int:
        minv= nums[0]
        print(minv)
        for i in range(len(nums)):
            
            if nums[i]< minv:
                minv= nums[i]
            minv=min(nums[i],minv)
        return minv
            
        