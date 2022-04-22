class NumArray:

    def __init__(self, nums: List[int]):
        self.dp=[0]
        for i in nums:
            #print(self.dp[-1]) prints in opposite order
            self.dp.append(self.dp[-1]+i)
            #print(self.dp[i])
            
        

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right+1]-self.dp[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)