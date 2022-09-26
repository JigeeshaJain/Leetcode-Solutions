class DetectSquares:

    def __init__(self):
        self.ptsCount=defaultdict(int)
        #we r using default dict as a hashmap coz its default value is 0 if the key isnt found 
        self.pts=[] #wer mainting a list as well which will keep a traack of the points added 
        

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)]+=1
        self.pts.append(point)
        #List cant be a key value for a hashmap in python so we need to convert it into tuple. IF it doesnt exist then itsdefault will be 0 e;se we will increment its value
        

    def count(self, point: List[int]) -> int:
        res=0 #no of ways in which squares can be formed 
        px,py=point
        for x,y in self.pts: #going through all possible diagonal values to the query point given. We need to verify whether it is a diagonal point 
           #iterate thr every x,y in the counts 
            if (abs(px-x))!=abs(py-y)or x==px or y==py:
                continue
            res+= self.ptsCount[(x,py)]*self.ptsCount[(px,y)] #we r checking point in our points map does that point exist and the opposite pint exist or not so we multiply each of it is 1 then 1*1 then we can create 1*1=1 square if it is 2 then 2*2=4 perfect squares we can create.
        return res
        
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)