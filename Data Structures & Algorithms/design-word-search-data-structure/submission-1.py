class TrieNode:
    def __init__(self) -> None:
        self.chico = {}
        self.endofword = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.chico:
                cur.chico[char] = TrieNode()
            cur = cur.chico[char]
        cur.endofword = True
        #HAD A COUPLE OF BUGS PLACING GLOBAL INSEAD OF LOCAL COPY OF ROOT IN dfs
        #blindly returning true instead of end of word at the end
        #and not passing child in the nest recursion of dfs

    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                char = word[i]
                if char != '.':
                    if char not in cur.chico:
                        return False
                    else:
                        cur = cur.chico[char]
                else:
                    for child in cur.chico.values():
                        if dfs(i+1,child):
                            return True
                    return False
                        
            return cur.endofword
        return dfs(0,self.root)