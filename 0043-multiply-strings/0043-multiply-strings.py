class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        p,x = 1,0
        for i in range(len(num1)-1,-1,-1):
          x = ((ord(num1[i])-ord("0"))*p)+x
          p*=10 

        p,y= 1,0
        for i in range(len(num2)-1,-1,-1):
          y=((ord(num2[i])-ord("0"))*p)+y
          p*=10 
        return str(x*y)
