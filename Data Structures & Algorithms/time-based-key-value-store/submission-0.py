class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        # get the values array for the specified key then perform the bin search operation on it
        values = self.store.get(key,[])#for default value
        #binary search
        l,r = 0 , len(values)-1
        while l<=r:
            mid = (l+r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0] #string add and try to find better value
                l = mid +1
            else:
                r = mid -1
        return res
        
