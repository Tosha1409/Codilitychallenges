#best greedy solution that i was able to find for task(code and speedwise), you cannot get maximum points cause it is too slow
def solution(X, Y):
    points = list(zip(X,Y))
    points.sort()
    minimum=max((points[1][0]-points[0][0]),abs(points[1][1]-points[0][1]))
    ln= len(points)
    for n in range (0,ln-1):
        m=n+1
        while (m<ln) and (points[m][0]-points[n][0]<minimum):
            cy=abs(points[m][1]-points[n][1])
            if cy<minimum:  minimum=max(cy,points[m][0]-points[n][0])
            if minimum <2 : return (0)
            m +=1
    return (minimum//2)