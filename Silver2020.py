def solution(A, B):
    #adding rectangle if it is matches.
    def update_results(number):
        if not (number in results): results[number]=1
        else: results[number]+=1

    #checking all rectangles.
    results = {}
    for rectangle in range(len(A)):
        update_results(A[rectangle])
        if A[rectangle]!=B[rectangle]: 
            update_results(B[rectangle])
            
    return max(list(results.values()))