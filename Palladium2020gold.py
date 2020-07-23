"""Simplier and faster approach without perfomance issues.
Calculations starts from assumption that only one banner used and of course height of banner equal to highest
building at set. Then we count case when one banner is 1 building long and rest is "highest banner", 2nd case
would be that first banner is 2 building long, and "highest" banner take rest and so on. Those calculations 
can be performed really easily, since height lenght of set is known, highest building know, and we check value 
of "current building" everytime and know highest building of other banner.
Then we invert array and perform same operations and get results for other side.
I am also optimized this approach, first i calculate values for minimal possible "highest" banners from left and
right and find limits to avoid useless extra calculations. For example, if we take set [1,2,3,10,8,5,10,7] we
need to count only 3 elements from left and 1 from right. """

def find_size(A): #finding banner size for covering A buildings
    if A==[]: return (0)
    else: return (max(A)*len(A))

def counting_first (A,highest): #finding started values (min of banners that have 1st and last highest building)
    left=find_size(A[:highest[-1]+1])+find_size(A[highest[-1]+1:])
    right=find_size(A[:highest[0]])+find_size(A[highest[0]:])
    return (min(left,right))

def solution(H):
    highest_building=max(H)
    highest=[H.index(highest_building), len(H)-(H[::-1].index(highest_building))-1]
    heights=[counting_first(H,highest)]
    full_banner=find_size(H)

    for side in (H[:highest[0]], H[highest[1]+1:][::-1]): #counting banners sizes
        height=0
        for c,x in enumerate(side,start=1):
            height=max(x,height)
            heights.append(full_banner-(highest_building*c)+(height*c))
    return (min(heights))