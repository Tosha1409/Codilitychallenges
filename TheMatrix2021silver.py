#Solution made with caterpillar method.
def solution(A):  
    result=0
    start=0
    end=0
    lowestnum=0
    lenA=len(A)

    while end<lenA and start<lenA-result:

        #finding/saving new minimum
        if A[end]<=A[lowestnum]: lowestnum=end

        #moving end if subsequence still bigger then minimal element.            
        if end-start+1<A[lowestnum] and A[lowestnum]>result:
            end += 1
            if end==lenA-1: result=max(result,end-start+1)
        
        #when minimal element is smaller then current subsequence(located in the end of subsequence).
        elif end-start>A[lowestnum] or A[lowestnum]<=result: 
            result=max(result,end-start)
            start=end=lowestnum=lowestnum+1

        else: 
            result=max(result,A[lowestnum])
            start=end=lowestnum=lowestnum+1

    return (result)