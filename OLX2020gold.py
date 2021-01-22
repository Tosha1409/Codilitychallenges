def solution(juice, capacity):
    #case when all drinks fits to same glass
    if sum(juice)<=max(capacity): return len(juice)

    #finding mixing glass and max capacity of other glasses
    max_capacity=-1 #free capacity of mixing glass
    max_capacity2=-1 #largest free capacity in other glasses
    max_juice=-1 #amount of juice in mixing glass
    #finding glass with largest free capacity and largest amount of juice.
    for x in range(len(juice)):
        space=capacity[x]-juice[x]
        if space>max_capacity:
                max_capacity=space
                max_juice=juice[x]
        elif space==max_capacity and max_juice<juice[x]: 
                max_juice=juice[x]
        else: max_capacity2=max(space,max_capacity2)

    #collecting juice from glasses that sorted in ascending order.
    counter=0
    filling=0
    juice.remove(max_juice)
    juice.sort()
    while filling<=max_capacity:
        filling += juice[counter]
        counter +=1

    #if mixing wasnt possible then checking possibility of mixing juice from mixing glass with juice from some other glass.
    if counter==1 and max_capacity2>=max_juice: return (2)
    
    return(counter)