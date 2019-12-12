coin,maximum,visited= [],[],[]

def find (x):
    if (x!=coin[x]): coin[x]=find(coin[x])
    return (coin[x])

def solution(A, B):
    n=len(A)
    for x in range(0,n+1):
        coin.append(x)
        maximum.append(x)
        visited.append(False)

    for x in range(0,n):
        if A[x]>n and B[x]>n: continue
        elif A[x]>n or B[x]>n or (B[x]==A[x]):
            f=b=find(min(A[x],B[x]))
        else: f,b=find(A[x]),find(B[x])
            
        if (f==b): visited[f]=1
        else:
            coin[f]=b
            if visited[f]==True: visited[b]=True 
            maximum[b]=max(maximum[f],maximum[b])
    
    result = n+1;
    for i in range (1,n+1): 
        if visited[find(i)]==False: result =min(result, maximum[find(i)])

    return (result)