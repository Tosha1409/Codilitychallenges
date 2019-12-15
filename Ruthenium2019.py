def solution(A, K):
    lenA=len(A) 
    results=K+1 #smallest possible result.
    #checking for exception when cases when all books for different ages.
    if lenA==K: return(K)
    elif lenA==len(list(dict.fromkeys(A))): return(K+1)
    books=[0]*(max(A)+1) #array with amount of books for every age.
    ages=[] #ages that included in currently checked subarray.
    start=end=0 #setting begining and end of subarray to first element.
    flag=1 #0 if we move start of array and 1 if we move end of it.
    
    while (end<lenA):
        #moving end of subarray
        if flag==1: 
            if books[A[end]]==0: ages.append(A[end])
            while (end<lenA-1) and (A[end]==A[end+1]):
                    books[A[end]] +=1
                    end +=1
            books[A[end]] +=1
        flag=0 #voiding flag for current round

        #checking if subarray and storing maximum result
        if len(ages)==1: results=max((end-start+K+1),results)
        for current in ages:
            if (end - start - books[current]+1)<=K: 
                flag=1
                results=max((end-start+1),results)
                break
            
        #moving start of subarray
        if flag==0: 
            while (A[start]==A[start+1]):
                books[A[start]] -=1
                start +=1
            books[A[start]] -=1
            if books[A[start]]==0: ages.remove(A[start])
            start +=1
        
        #moving end of subarray (if there was some result in current one)
        if flag==1: end +=1

    return(min(results,lenA))