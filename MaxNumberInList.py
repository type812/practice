lst = []
num = int(input("How many numbers: "))

for n in range(num):
    numbers = int(input('Enter numbers: '))
    lst.append(numbers)

print('Maximum element in the list is: ',max(lst))
