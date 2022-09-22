class TimeMap:

    def __init__(self):
        self.store={} #key: list of list [value, timestamp]
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]  # if there is no value in the list we will initialize a new list as it is a list of lists
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res="" # this is done coz if we dont find key default value is ""
        values=self.store.get(key,[]) #if it find the match it will return the list if it doesnt find the list it will by default return an empty list
        
        #Binary search
        l,r=0, len(values)-1
        
        while l<=r:
            m=(l+r)//2
            if values[m][1]<= timestamp:
                res =values[m][0]
                l=m+1
            else:
                
                r=m-1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
