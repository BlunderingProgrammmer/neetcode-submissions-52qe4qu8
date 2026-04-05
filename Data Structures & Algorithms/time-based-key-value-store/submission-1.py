class TimeMap:

    def __init__(self):
        self.storemap = collections.defaultdict(list)#saves some lines of code on set; key : [[values,timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storemap[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.storemap.get(key,[])#using get fuction to get all the list of values for the key else seting a default value
        l,r = 0,len(values)-1
        while l<=r:#small cahnge to make binseearch more eff and readable
            m = (l+r) // 2
            if values[m][1] == timestamp:
                res = values[m][0]
                return res
            elif  values[m][1] < timestamp:
                res = values[m][0]    
                l = m +1
            else:
                r = m-1
        return res   
