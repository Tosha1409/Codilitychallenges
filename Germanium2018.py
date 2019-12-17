card,maximum,visited= [],[],[]

def find (x): #finding maximum and marking 
    if (x!=card[x]): card[x]=find(card[x])
    return (card[x])

def solution(A, B):
    n=len(A) #initialization and filling arrays
    for x in range(0,n+1):
        card.append(x)
        maximum.append(x)
        visited.append(False)

    for x in range(0,n):
        if A[x]>n and B[x]>n: continue #pass if front and back side of card value too big
        elif A[x]>n or B[x]>n or (B[x]==A[x]): #if only one side of card fits
            f=b=find(min(A[x],B[x]))
        else: f,b=find(A[x]),find(B[x]) #both sides of card fits
        #main part that make changes    
        if (f==b): visited[f]=True
        else:
            card[f]=b
            if visited[f]==True: visited[b]=True 
            maximum[b]=max(maximum[f],maximum[b])
    
    #finding final result
    result = n+1;
    for i in range (1,n+1): 
        if visited[find(i)]==False: result =min(result, maximum[find(i)])

    return (result)