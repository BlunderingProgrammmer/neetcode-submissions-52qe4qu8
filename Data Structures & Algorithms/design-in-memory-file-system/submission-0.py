import bisect
class FileSystem:

    def __init__(self):
        #2 hashmaps needed 
        self.paths = collections.defaultdict(list) #"directory" -> [list of its children]
        self.filenames = collections.defaultdict(str) #"filename "->value (string)

    def ls(self, path: str) -> List[str]:
        if path not in self.filenames:#if its a directory path
            return self.paths[path]
        return [path.split("/")[-1]]

    def mkdir(self, path: str) -> None:
        directories = path.split("/") #will return a list ["","a","b"]etc
        for i in range(1,len(directories)):#1 cuz to skip the empty string in directories
            cur = "/".join(directories[:i]) or "/"#will check first to be true on base case it will be / for parent direcctory
            #there are two conditions
            #case 1- cur is not in paths -just add ..defdict takes care of def case
            #case2 -cur in paths but does not have its sub dict in the values section-same just add but with sorted order
            if cur not in self.paths or directories[i] not in self.paths[cur]:
                bisect.insort(self.paths[cur],directories[i]) #args -where u are inserting and what            
    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.filenames:
            self.mkdir(filePath)
        self.filenames[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.filenames[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
