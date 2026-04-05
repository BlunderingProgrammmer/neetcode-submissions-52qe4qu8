class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line ,length = [],0 #keeping line as a array makes it easier to count no of words,while length counts no of charecters
        i = 0
        while i < len(words):
            #2 cases one where the line is complete and other where its not and words can be added
            #now if line is complete and we need to allocate space to it
            #first if check
            if length + len(line) + len(words[i]) > maxWidth:#here len(line) give no of mandatory spaces(1 for each with one safety buffer)
                spaces = maxWidth - length # give all the spaces left for the line

                mandatory_space = spaces // max(1,len(line)-1) 
                #mandatory space means 1 space in between each words hence len-1,max 1 is edgs case to prevent div by 0
                remainder_space = spaces % max(1,len(line)-1)# space for greedy allocation 
                for j in range(max(1,len(line)-1)): #len()-1 gives no words,1 prevents edges case of only one large words in line not excuting
                    line[j] += " " * mandatory_space   #assigns the mandatory no space to each words 
                    if remainder_space:#if remainder_space exists then add greedy from left to rightstoping before the end
                        line[j] += " " # if u multiply by entire remainder space then its not even
                        remainder_space -=1  
                res.append("".join(line))
                #remember to reset line after each successfull inclusion to res
                line ,length = [],0
            #handle adding words first
            line.append(words[i])
            length+= len(words[i])
            i+=1
        #for the last line - left justify and it will never exceute on the above loop
        last_line  = " ".join(line) # how this is found is that on the last iteration of the while loop those 3 lines will 
        #run and if block will never excute  hence seperate handling
        trailing_space = maxWidth -  len(last_line)
        res.append(last_line + " " *trailing_space)
        return res 