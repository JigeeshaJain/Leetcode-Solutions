class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n]=1+count.get(n,0)
        for n,c in count.items():
                freq[c].append(n)    #here it says that c ie. the freq we are adding the list of elemets that have occured c times. so count is the index and values are the list of elements with that frequency.
        res=[]
        for i in range(len(freq)-1, 0,-1): 
                
                #here we r gng in reverse order as we need the K most freq elements and for that we need to start with the highest number of the element range(start,stop, step)
                
                 for n in freq[i]:
                    res.append(n)
                    if len(res)==k:
                        return res
                    
        
        
       