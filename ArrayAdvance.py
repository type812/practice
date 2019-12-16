def arrayAdvance(A):
    furthest_reached = 0
    last_indx = len(A) - 1 #len -1 will give tha least index
    i = 0 #iterator

    while i<=furthest_reached and furthest_reached < last_indx:
        furthest_reached = max(furthest_reached, A[i]+i)
        i+=1
    return furthest_reached >= last_indx
    #return furthest_reached


A1 = [3,3,1,0,2,0,1]
A2 = [3,2,0,0,2,0,1]
print(arrayAdvance(A1))