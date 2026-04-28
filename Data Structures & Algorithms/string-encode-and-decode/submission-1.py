class Solution:

    def encode(self, strs: List[str]) -> str:
        #output is  a single large string with all the words
        res = ''
        for string in strs:
            res += str(len(string)) + '#' + string
        return res

    def decode(self, s: str) -> List[str]:
        res,i = [],0 #the i is just an iterator that keeps track of which word we are at
        while i < len(s):#while i is still in bounds of the giant string
            j = i
            while s[j] != '#':
                j+=1
            length_of_string = int(s[i:j]) #get length of string j not included
            single_word = s[j+1 : j+1+length_of_string] #j is on # so + 1+ length to get to end of word
            res.append(single_word)#append result
            i = j+1+length_of_string #error before use = instead of += bug on longer inputs
        return res
