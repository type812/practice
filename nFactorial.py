
#num= int(input('Enter number to find factorial: '))

def factofN(num):
    fact = 1
    if num<0:
        print("Factorial of -ve numbers don't exist")
    elif num ==0:
        print("Factorial is 1")
    else:
        for i in range(1,num+1):
            fact = fact*i
        print(fact)

factofN(3)