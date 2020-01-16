#read vs readlines
count = 0
def fileSearch():
    with open('Nutanix Interview.txt','r') as f:
        if 'questions' in f.read():
            return True
    return False

if fileSearch():
    print('True')
else:
    print('False')

