'''
pair_sum([1,3,2,2],4)
would return 2pairs:
(1,3)
(2,2)
'''

def pair_sum(arr,k):
    if len(arr)< 2:
        return print("too small to perform pair sum")

    seen = set()
    output = set()

    for num in arr:
        target = k-num

        if target not in seen():
            seen.add(num)

        else:
            output.add(min(num, target),max(num, target))

    print('\n'.join(map(str,list(output))))

pair_sum([1,3,2,2],4)