# function to check if small string is
# there in big string
def check(string, sub_str):
    if (string.find(sub_str) == -1): #using find command 
        print("NO")
    else:
        print("YES")

    # driver code


string = "geeks for geeks"
sub_str = "geek"
check(string, sub_str)