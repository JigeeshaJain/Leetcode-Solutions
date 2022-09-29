class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        print(nums)
        a=len(nums)
        print(a)
        c=a-k
        print(c)
        for i in range(len(nums)):
            if i==c:
                return nums[i]
            continue
        
            
        