from re import search
import re
def check_substring(str, sub):
    #using regex
    if search(sub,str):
        print('Found')
    else:
        print('not found')

#check_substring('stackabuse','tak')

#######################
str1 = '''
#numbers
123-1234-111
345.5433.132
800.5433.132
900.5433.132
'''
#pattern = re.compile(r'\d{3}.\d{4}.\d{3}')
pattern = re.compile(r'[89]00.\d{4}.\d{3}')
matcher = pattern.finditer(str1)
for match in matcher:
    print(match)

############
#match everything but bat in the given sentence
sent = '''
cat
pat
bat
mat
sat
'''
pattern1 = re.compile(r'[^b]at') #everything but 'bat' hence the carrot
matcher1 = pattern1.finditer(sent)
for match in matcher1:
    print(match)

#Name and title founder pattern
s = '''
Mr. Srivastava
Mr Smith
Ms David
Mrs. Robinson
Mr. T
'''

pattern2 = re.compile(r'(Mr| Ms|Mrs)\.?\s[A-Z]\w*') #() -grouping
matcher2 = pattern2.finditer(s)
for match in matcher2:
    print(match)


#Finding all email addresses in a file or string
em='''
anit.8923@gmail.com
fef@bb.com
fefgreg@765.com
fefgreg@765.net
fefgreg@765.edu
'''
pattern3 = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z0-9]+\.(com|net|edu)')
matcher3 = pattern3.finditer(em)
for match in matcher3:
    print(match)

#password matcher regex (nice example)

str1='P@ssord123'
if re.match("[a-zA-Z0-9.]+", str1) and len(str1) > 0 and len(str1)<=64:
    if len(str1)>=10 and re.search("[0-9]+",str1) and re.search("[A-Z]+",str1) and re.search("[a-z]+",str1):
        print("True")
    else:
        print("False")


#search for special characters in a string using regex
str2 ='adn@fj#%$'
#m = re.compile(r'[^\w\*]')
lst = re.findall(r'[\W\*]',str2)
print(list(lst))
#m = re.compile(r'[\W\*]')
#mat = m.finditer(str2)

#for mat1 in mat:
    #print(mat1)