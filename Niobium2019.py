#creating inverted string cause inverted strings after changes would fit to condition as well (n alwasy given to
#save time.
def invert (array, n):
    result=[]
    for x in range(0,n):
        if array[x]==0 : result.append(1)
        else: result.append(0)
    return (result)

def solution(A):
    row_len=len(A[0]) #len of row.
    if row_len==1 or len(A)==1: return (len(A)) #expections that don't need calculation.
    score=0
    A.sort()

    while (len(A)>score): #continue till amounts of rows in matrix is bigger then current biggest score.
        current=A[0] 
        current_inverted=invert(current,row_len)
        current_score=0
        x=0
        while (x<len(A)): #searching for string and inverted string and removing them from matrix.
            if A[x]==current or A[x]==current_inverted:
                current_score +=1
                A.pop(x)
            else: x+=1
        score=max(score, current_score)
    
    return(score)