from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1=Counter(s1)
        l1=len(s1)
        l2=len(s2)
        for i in range(0,l2-l1+1):
            if Counter(s2[i:i+l1])==c1:
                return True
        else:
            return False 
                   
                   
                   
            
        