def solution(X, Y):
    #probably best way to unite and sort two arrays
    points = list(zip(X,Y))
    points.sort()
    #creating empty dictonary P and finding distance beetween first two points
    minimum=max((points[1][0]-points[0][0]),abs(points[1][1]-points[0][1]))
    P ={}
    #filling dictonary where is key is X coordinate and value is array with all Y coordinates with same X
    for x in points:
        if x[0] in P: P[x[0]].append(x[1])
        else: P[x[0]] = [x[1]]
    #getting all keys and storing them
    xpoints=list(P.keys())
    #loop that goes through all possible X coordinates. Some values stored in valuable for incresing speed.
    for x in range(0,len(xpoints)):
        ax=xpoints[x]
        ypoints=P[ax]
        #loop for Y coordinates
        for y in range(0,len(ypoints)):
            #finding closest point where is X same and only Y is different
            if (y<len(ypoints)-1) and (ypoints[y+1]-ypoints[y]<minimum): minimum=ypoints[y+1]-ypoints[y]
            ystart=ypoints[y]
            yb1=ypoints[y]-minimum
            yb2=ypoints[y]+minimum
            m=x+1
            #3rd loop for finding points with different X that have delta X and Y smaller then minimum
            while (m<len(xpoints)) and (xpoints[m]-ax<minimum):
                for z in sorted(x for x in P[xpoints[m]] if yb1<x<yb2): 
                    minimum=max(abs(z-ystart), xpoints[m]-ax)
                m +=1
    return(minimum//2)