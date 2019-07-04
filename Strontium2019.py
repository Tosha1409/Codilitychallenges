#finding array index based on letter
def array_index(a):
    return (ord(a)-97)

def solution(words):
    #initializing two dimmensioned array with results it have 26 elements(amounts of letter in alphabeth)
    #and 4 elements for every letter, where is 1st is maximal prefix lenght, 2nd - amount of elements in 
    #strings that consists of same letter, 3rd - maximal suffix, and 4th is biggest lenght of prefix in 
    #word where is suffix and prefix are exactl same. and middle is longest substring at any place
    results = [[0] * 4 for i in range(26)]
    middle=0
    
    #checking word after word 
    for word in words:
        #if word cosist of one letter then adding 1 to strings that consist of same letter
        if len(word)==1: results[array_index(word)][1] +=1
        #otherwise counting lenght of substrings
        else:
            n=c=count=0
            letter=word[0] #first symbol of word
            #if current symbol is not same
            while (c<len(word)): 
                if letter!=word[c]: 
                    #changing symbols for searching substring
                    letter=word[c]
                    middle=max(middle,count) #checking/saving longest substring
                    if n==0: n=count #saving if it prefix as prefix
                    count=0 #voiding substing symbol counter
                c+=1 #increasing letter number
                count+=1 #increasing substring lenght counter
            m=count #saving suffix when loop is ended
            #adding lenght to result array if string included same symbol.
            if (count==len(word)): results[array_index(word[0])][1] += count
            #otherwise sorting our results
            else:
                #if suffix and prefix strings have different letters, then saving both
                #if theirs values bigger then ones at resulsts array
                if word[0]!=word[-1]:
                    results[array_index(word[0])][0]=max(results[array_index(word[0])][0], n)
                    results[array_index(word[-1])][2]=max(results[array_index(word[-1])][2], m)
                #if suffix and prefix have same letter
                else:
                    i=array_index(word[0])
                    #if prefix is bigger, then trying to save it in resulsts otherwise saving suffix 
                    if (n>m):
                        if (results[i][0] < n): results[i][0] = n        
                        elif (results[i][2] < m): results[i][2] = m
                    #is suffix is bigger then doing it in opposite way
                    elif(m>n):
                        if (results[i][2] < m): results[i][2] = m
                        elif (results[i][0] < n): results[i][0] = n        
                    #if them are equal then saving value at 4th element if it is bigger then previous one
                    #and adding smaller value of 4th element to suffix or prefix
                    else:
                        n, results[i][3] = min(n,results[i][3]), max(n,results[i][3])
                        if (results[i][0]<=results[i][2]) and (results[i][0]<n): results[i][0]=n
                        elif (results[i][2]<results[i][0]) and (results[i][2]<n): results[i][2]=n
                            
    #counting and returning results
    m=0
    for x in results: m=max(m, (sum(x)-min (x[0] ,x[2], x[3]) ) )
    m=max(middle,m) #comparing result also to longest substring
    return(m)