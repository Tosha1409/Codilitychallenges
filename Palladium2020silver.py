"""Original solution attempt that failing 3 perfomance tests, but i decided to finish it,
because I like algorithm idea that was used. So here is the description:
1. When you cover any amount of buildings with two banners, one of them must be high as 
highest building and can be from left or right side of array. So this means that smallest
possible highest banner can start left side and end at most right highest building, or
start at right and end at most left highest building.
2. Cases with smallest highest banner is not always "right" choice, because banner from 
other side would be as high as highest building that it covers. And sometimes sum of banners
sizes would be smaller if you use longer highest banner, because 2nd banner might be lower/
smaller in this case.
3. Smallest sum can be found in following way: first taken smallest "high" banner from left
side (or right side, order doesnt matter) and count size of 2nd banner and sum of both banners.
Next step we assume that "high" banner covers most right building of 2nd banners, and recount
size of second banner. Those operations repeated till end is reached. After that we do same
operation starting from smallest banner on right side and moving left. So one of those results
will be minimum sum that we are looking for.
4.This approach will for fine for most of cases and looks elegant, but for example array like 
[1,2,3,10,9,2,1] will cause serious perfomance issues. """

def solution(A):

    def find_height(A): #finding banner size for covering A buildings
        if A==[]: return (0)
        else: return (max(A)*len(A))

    def count_left(A,highest): #case when left side have biggest banner
        return (find_height(A[:highest[-1]+1])+find_height(A[highest[-1]+1:]))

    def count_right(A,highest): #case when right side have biggest banner
        return (find_height(A[:highest[0]])+find_height(A[highest[0]:]))

    def counting (A,highest): #minimum of both cases
        return(min(count_left(A, highest), count_right(A,highest)))

    def step_left(A, highest): #moving left till next highest building(that lower then previous one)
        if highest[0]!=0: 
           new_highest=max(A[:highest[0]])
           highest[0]=A.index(new_highest)
        return(highest)

    def step_right(A, highest): #moving right
        if highest[1]!=len(A)-1:
           new_highest=max(A[highest[1]+1:])
           highest[1]=len(A)-1-A[::-1].index(new_highest)
        return(highest)

    highest_building=max(A) #finding higest building in set
    #set of 1st and last highest building
    original_highest=[A.index(highest_building), len(A)-(A[::-1].index(highest_building))-1]
    final_result=original_result=counting(A,original_highest)

    #moving left
    highest=original_highest[:]
    while highest[0]!=0:
        highest, result=step_left(A,highest),count_right(A,highest)
        if result<final_result: final_result=result

    #moving right
    highest=original_highest[:]
    while highest[1]!=len(A)-1:
        highest, result=step_right(A,highest), count_left(A,highest)
        if result<final_result: final_result=result
    
    return (final_result)