def solution(A, B, F):
    C=[] #There will be two dimmensioned array where is every element [productivity in A team, difference in productivity]
    team1=team2=0 
    for x in range(0,len(A)): C.append([A[x]-B[x],A[x]]) #filling C
    C.sort(reverse=True)
    for x in range(0,F): team1 += C[x][1] #counting productiviy in team1
    for x in range(F,len(A)): team2 += C[x][1]-C[x][0] #counting productiviy in team2
    return (team1+team2)