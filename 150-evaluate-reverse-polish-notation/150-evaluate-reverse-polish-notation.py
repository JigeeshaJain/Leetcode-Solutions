class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            
            if i =="+":
                stack.append(stack.pop()+stack.pop())
                
            elif i =="-":
                a=stack.pop()
                b=stack.pop()
                c=b-a
                stack.append(c)
            
            elif i== "*":
                stack.append(stack.pop()*stack.pop())
            elif i =="/":
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a)) #to convert it to whole number
            else:
                stack.append(int(i))
        return stack[0]
                
