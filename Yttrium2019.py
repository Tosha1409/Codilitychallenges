#creating new element substring that including two other substrings [begining, end, lenght]
def create_element (a,b):
    e1=min(a[0],b[0])
    e2=max(a[1],b[1])
    return ([e1,e2,e2-e1+1])

def solution(S, K):
    #creating of two dimensioned array 
    results = []
    n=len(S)
    for x in range (0,26): results.append([-1]*3)
    #going through string and counting first and last matches to letter and storing results to array
    for x in range(0,len(S)): 
        m=ord(S[x])-97
        if results[m][0]==-1: results[m][0]=results[m][1]=x
        else: results[m][1]=x
    #removing empty elements from results and counting lenght
    x=0
    while (x<=len(results)-1):
        if results[x][0]==-1: results.pop(x)
        else: 
            results[x]=create_element(results[x],results[x])
            x += 1
    #searching result. first expections that doesnt needs counting
    if len(results)<K: n=-1
    elif (len(results)==K): n=0
    elif (K==0): n=len(S)
    #and finally rest of cases
    else:
        rounds=len(results)-K-1 #amount of rounds minus one, because last round is searching for final result
        results.sort() #sorting array to avoid mess in calculations
        for x in range(0,rounds):
            tmp=[]
            for y in range (0,len(results)-1):
                localmin=[0,n-1,n] #full string/largest possible substring
                for z in range(y+1,len(results)):
                    element=create_element(results[y],results[z])
                    if element[2]<localmin[2]: localmin=element
                tmp.append(localmin) #storing smallest possible sum of substrings
            results = tmp #storing results for next round
        #last round/finding result
        for x in results: n=min(n,x[2])
    return (n)