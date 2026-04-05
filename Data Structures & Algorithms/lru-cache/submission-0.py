class Node:
    def __init__(self,key,value):
        self.key , self.value = key , value
        self.prev,self.next = None,None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        #create two dummy nodes to know where LRU and MRU are 
        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next ,self.right.prev = self.right,self.left
    #write 2 helper functions to help in insertion and removal for LRU and MRU
    #remove fuction to help remove node from list
    def remove(self,Node):
        prev,nxt = Node.prev,Node.next
        prev.next ,nxt.prev = nxt,prev
    #insert add node to lRU class ll basically shifting LRU and MRU
    def insert(self,Node):
        prev , nxt = self.right.prev,self.right
        prev.next , nxt.prev = Node,Node
        Node.prev , Node.next = prev,nxt
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        #if in hash remove else and add
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]

        
