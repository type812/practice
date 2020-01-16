'''
take an array with +ve and -ve integers and return max sumof the array
'''

def returnMaxSum(arr):
    if len(arr)==0:
        print('Too small ')

    max_sum = curr_sum = arr[0]

    for num in arr[1:]:
        curr_sum = max(curr_sum+num , num)
        max_sum = max(curr_sum,max_sum)


    return max_sum

print(returnMaxSum([1,2,-4,5,7,12]))