class Solution {
    public int getSum(int a, int b) {
        while (b!=0){
            int temp=(a & b) << 1; //will save the original value of a and we r left   shifting in order to take care of carry 
            a= a ^ b; 
            b= temp;
                
        }
        return a;
        
        
        
    }
}