def solution(N, Q, B, C):
    counters = []
    if Q<=1: return (0) #exception when required just one ball
    if max(C)>0: #for all cases
        for x in range (0,N): counters.append({})
        for x in range (0,len(C)):
            if C[x] in counters[B[x]]:  counters[B[x]][C[x]] += 1
            else: counters[B[x]][C[x]] = 1
            if counters[B[x]][C[x]] == Q: return (x) 
    else: #for cases with one colour
        counters= [0]*N
        for x in range (0,len(C)):
            counters[B[x]] +=1
            if counters[B[x]]==Q: return(x)
    return (-1)