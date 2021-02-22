def solution(A):
    result=0
    start=0
    end=0
    lowestnum=0 #number of smallest element in current subsequence.         
    rising=0 #ending number of increasing subsequence in current subsequance.
    lenA=len(A)

    while end<lenA and start<lenA-result:

        #finding/saving new minimum.
        if A[end]<=A[lowestnum]: lowestnum=end

        #moving end if subsequence still bigger then minimal element(also finding limits of increasing subsequence).            
        if end-start+1<A[lowestnum] and A[lowestnum]>result:
            if A[end]<A[end+1] and end==rising: rising +=1
            end += 1
            if end==lenA-1: result=max(result,end-start+1)

        #checking/saving current results for current subsequence and setting new start and end.        
        else:
            result=max(result,end-start,A[lowestnum])
            start=lowestnum=lowestnum+1
            rising=end=max(start,rising,lowestnum+1)
            if start==end:end=rising=end+1
                
    return (result)