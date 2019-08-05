def solution(K, M, A):
    leader=(len(A)//2)+1
    #counting, current K, max increment
    numbers=[[0]*(M+2),[0]*(M+2),[0]*(M+2)]
    results=[]
    for x in range(0,len(A)):
        numbers[0][A[x]-1]+=1 #incrementing counter for number in array 
        numbers[1][A[x]]+=1 #incrementing counter of number+1 (when numbers belongs to K) 
        numbers[1][A[x]-1]-=1 #removing number from K, if number becomes number plus 1, it means that there is less instances of number itself
	
	#when we are working with first possible K subarray(0..K),we just copy values from numbers[1] to numbers[2]
        if x<K:
            numbers[2][A[x]]=numbers[1][A[x]]
            numbers[2][A[x]-1]=numbers[1][A[x]-1]

	#when we are working with next possibnle K subarrays
        if x>=K:
	    #removing previous first element
            numbers[1][A[x-K]]-=1
            numbers[1][A[x-K]-1]+=1
	    #finding possible maximal amount of instances of number in K-subarray
            numbers[2][A[x]]=max(numbers[2][A[x]], numbers[1][A[x]] )
            numbers[2][A[x-K]-1]=max(numbers[2][A[x-K]-1], numbers[1][A[x-K]-1] )

	#checking if there is new leader and adding it to results
        if numbers[0][A[x]]+numbers[2][A[x]]>=leader and (A[x]+1 not in results): results.append(A[x]+1)
        if numbers[0][A[x]-1]+numbers[2][A[x]-1]>=leader and (A[x] not in results): results.append(A[x])
            
    results.sort()
    return (results)