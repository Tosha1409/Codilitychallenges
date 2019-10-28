def solution(A):
    start=0 #start - most left row that possible in current round.
    result=A[0][0] #results. First(0) and last rounds skipped, because first round value is basicly A[0][0].
    n,m=len(A[0]),len(A) #size of matrix.
    moves = n+m-2 #amount of possible rounds.
    maxnumbers=[0] #numbers of rows with biggest element from previous round. 0 - value after first round.
    if n==m==1: return str(result) # returning result if there is only one round possible.

    #next rounds    
    for i in range (1,moves):
        currentmax=0         
        currentmaxnumbers = [] #reseting values for next round
        if i>m-1: start = i-m+1 #if height limit of matrix reached then we move right
        for j in range (start,min(i+1,n)):
            if ((j) in maxnumbers) or ((j-1) in maxnumbers): #if current cell is neighbourgh of cells from previous round
                if (A[i-j][j]>currentmax): #new maximum element
                    currentmax = A[i-j][j]
                    currentmaxnumbers = [j]
                elif (A[i-j][j]==currentmax): currentmaxnumbers.append(j) #next maximum element
        result = result*10+currentmax
        maxnumbers=currentmaxnumbers
        
    result=result*10+A[-1][-1] #adding results of last round
        
    return str(result)