def decorated_function(originial_function):
    def wrapper_function():
        print('Wrapper fucntion executed {}'.format(originial_function.__name__))
        return originial_function()
    return wrapper_function()

def display():
    print("Display function ran")

decorated_display = decorated_function(display)
decorated_display


'''
Using the @ annotation 
'''

def decorated_function(originial_function):
    def wrapper_function():
        print('Wrapper fucntion executed {}'.format(originial_function.__name__))
        return originial_function()
    return wrapper_function()

@decorated_function
def display():
    print("Display function ran")

display