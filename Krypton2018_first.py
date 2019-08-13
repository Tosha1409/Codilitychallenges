#minimizing numbers (and if it have zeros then them are kept)
def change_number(n):
    if n==0: return(0)
    zeros=1
    if (n%10)==0:
        zeros=int('1'+zeros_amount(n)*'0')
        n=n/zeros
    if (n%5)==0: n=5
    elif (n%2)==0: n=2 
    else: n=1
    return (n*zeros)

#counting amount of zeros in a number    
def zeros_amount(n):
    return (len(str(n)) - len(str(n).rstrip('0')))

#finding minimum number with minimum amount of zeros    
def find_min(n,m):
    nzeros, mzeros =zeros_amount(n),zeros_amount(m)
    if (nzeros<mzeros): return(n)
    elif (nzeros==mzeros) and n<m: return(n)
    else: return(m)

def solution(A):
    N=len(A)
    zero_included=0
    #creating first 1st line(it is different from other lines)
    firstline=A[0]
    for x in range(1,N): firstline[x] = change_number(firstline[x-1]) * change_number(firstline[x])

    m=1
    while m<N:
        secondline=A[m]
        newline=[]
        for x in range(0,N):
            secondline[x]=change_number(secondline[x])
            if (x==0): newline.append(firstline[0]*secondline[0])
            elif (secondline[x]==0): 
                zero_included=1
                newline.append(0)
            else:
                newline.append(find_min(firstline[x]*secondline[x],secondline[x]*newline[-1]))
        firstline=newline
        m +=1
    
    #finding result(last number in array), and comparing it to 1 if there was there was 0 element somewhere
    result=zeros_amount(firstline[-1])
    if zero_included!=0: result=min(result,1)
    return(result)