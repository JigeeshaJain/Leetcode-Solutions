class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output=[intervals[0]]  #adding 1st element to the output array
        print(intervals)
        
        for start, end in intervals[1:]:
            lastEnd=output[-1][1]
            print(lastEnd)
            
            if start<=lastEnd:
                output[-1][1]=max(lastEnd,end)
            else:
                output.append([start,end])
                
        return output
        
        