#minimizing numbers and counting zeros
def change_number(n):
    if n==0: return([0,1])
    zeros=0
    if (n%10)==0:
        zeros=zeros_amount(n)
        zero=int('1'+zeros*'0')
        n=n/zero 
    if (n%5)==0: n=5
    elif (n%2)==0: n=2 
    else: n=1
    return ([n,zeros])
    
#counting amount of zeros in a number    
def zeros_amount(n):
    return (len(str(n)) - len(str(n).rstrip('0')))

#finding smaller number with minimum amount of zeroes    
def find_min(n,m):
        if m[0]==n[0]==0: return ([0,1])
        if m[0]==0 or n[1]<m[1]: return(n)
        elif n[0]==0 or m[1]<n[1]: return (m)
        elif n[0]<m[0]: return (n)
        else: return(m)

#multiple two array elements
def mult(a,b):
    if a[0]==0 or b[0]==0: return([0,1])
    first,second= a[0]*b[0], a[1]+b[1]
    if first%10==0: 
        first=first//10
        second+=1
    return [first,second]
    
def solution(A):
    N=len(A)
    zero_included=0

    #creating first 1st line(it is different from other lines
    firstline=A[0]
    firstline[0]=change_number(firstline[0])
    for x in range(1,N): firstline[x] = mult(firstline[x-1], change_number(firstline[x]))

    m=1
    while m<N:
        secondline=A[m]
        newline=[]
        for x in range(0,N):
            secondline[x]=change_number(secondline[x])
            if (x==0): newline.append(mult(firstline[0],secondline[0]))
            elif (secondline[x][0]==0): 
                zero_included=1
                newline.append([0,1])
            else:
                newline.append(find_min(mult(firstline[x],secondline[x]),mult(secondline[x],newline[-1])))
        firstline=newline
        m +=1

    #finding result(zeros in last element of array), and comparing it to 1 if there was there was 0 element somewhere
    result=firstline[-1][1]
    if zero_included!=0: result=min(result,1)
    return(result)