def solution(P):
    limiter=result=0
    l=len(P)
    
    for x in range (0,l):
        if P[x]==True: 
            result += (l-x)*(x+1-limiter)
            limiter=x+1

    return(min(result, 1000000000))