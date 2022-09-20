class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r =0,len(nums)-1
        res=nums[0]
        while l<=r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m=(l+r) //2
            res=min(res,nums[m])
            if nums[m]>= nums[l]:
                l=m+1 #coz its rotated all the elements in right sorted section will be smaller to the elements in the left sorted array. eg:[3,4,5,1,2] m=index(5)
            else:
                r=m-1
        return res
                
        
        
        #minv= nums[0]
        #print(minv)
        #for i in range(len(nums)):
            
            #if nums[i]< minv:
                #minv= nums[i]
           # minv=min(nums[i],minv)
        #return minv
            
        