class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashmap={")":"(","}":"{","]":"["}
        
        for c in s:
            if c in hashmap:
                if stack and stack[-1]==hashmap[c]: #making sure that the stack has opening element i.e. it is not empty as we cant add closing parenthesis to empty stack also checking whether the last added character in stack i.e. stack[-1] matches the closing brace in the hashmap so that we r checking the opening brace and matching it to the entry in the hashmap. If it satisfies the condition we have found the pair and so we pop the pair  
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False       
                
        