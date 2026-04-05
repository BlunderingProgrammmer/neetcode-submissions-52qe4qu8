class TrieNOde():
    def __init__(self):
        self.children = {}
        self.endofword = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNOde()

    def insert(self, word: str) -> None:
        cur = self.root #put the cur label on root node initialized on the constructor 
        for c in word: #for each char in word
            if c not in cur.children:#check if it is in the tree level
                cur.children[c] = TrieNOde()#if not create a node for it
            cur = cur.children[c] #IF IT EXIST THEN TRAVERSETO IT 
        #mark end of the word after loop has ended
        cur.endofword = True
    def search(self, word: str) -> bool:
        cur = self.root #put the cur label on root node initialized on the constructor 
        for c in word: #for each char in word
            if c not in cur.children:#check if it is in the tree level
                return False#if not return False
            cur = cur.children[c] #IF IT EXIST THEN TRAVERSETO IT 
        #at the end of the traversal return true if it is end of word
        return cur.endofword
    def startsWith(self, prefix: str) -> bool:
        cur = self.root #put the cur label on root node initialized on the constructor 
        for c in prefix: #for each char in word
            if c not in cur.children:#check if it is in the tree level
                return False#if not return False
            cur = cur.children[c] #IF IT EXIST THEN TRAVERSETO IT 
        #at the end of the traversal return true if it reached the end safely
        return True