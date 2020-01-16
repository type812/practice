
#not so perfect solution.
#move all non-zeros to the left and zeroes will be left out at the right.
def pushNonZeroRight(arr,n):
    c= 0
    for i in range(n):
        if arr[i]!= 0:
            arr[c] = arr[i]
            c=c+1
        while c<n:
            arr[c]=0
            c=c+1
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
print(arr)
n = len(arr)
pushNonZeroRight(arr,n)
print(arr)

####
def zero_back(alist):
    count=0
    for i in alist:
        if i == 0:
            count=count+1
    for i in alist:

        if i == 0:
            alist.remove(i)
    for _ in range(count):

        alist.append(0)
    return alist

print(zero_back())