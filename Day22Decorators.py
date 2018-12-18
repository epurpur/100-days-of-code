#from functools import wraps


def outer_func(msg):
    message = msg
    print(message)
    
    def inner_func(msg2):
        #print(message)
        print(msg2)
        
    return inner_func

#hi_func = outer_func("printing outer function")  #msg is argument passed to outer_func. In this case, 'hi'

#hi_func("printing inner function")    #msg2 is parameter passed to inner_function. In this case, 'hello'

"""

def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function                     #this is the same as display=decorator_function(display) below
def display():
    print('display function ran')

#display = decorator_function(display)  # this is exactly the same as @decorator_function above
#display()
"""

"""

def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

#@decorator_function                     #this is the same as display=decorator_function(display) below
def display():
    print('display function ran')

display = decorator_function(display)  # this is exactly the same as @decorator_function above
display()
"""

"""
def outer_function(other_function):
    print("printing from outer_function")
    
    def inner_function():
        print("printing from inner function")
        return other_function()
    return inner_function

@outer_function
def extra_func():
    print("printing from extra function")

#my_func = outer_function(extra_func)
#my_func = outer_function('ho')  #passing argument 'ho' to outer_function
extra_func()             #passing variable msg2 to inner function
"""

text_to_include = 'i code with pybites'

def make_html_tag1(func):
    def wrapper(tag1):
        print(f'<{tag1}>')
        func()
        print(f'</{tag1}>')
    return wrapper

def make_html_tag2(func):
    def wrapper(tag1):
        print(f'<{tag1}>')
        func()
        print(f'</{tag1}>')
    return wrapper

@make_html_tag2
def get_text(text=text_to_include):
    print("input text: ", text)
    #return(text)

#full_html = make_html(get_text)
#get_text('strong')

#Python decorator thread: https://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators#answer-1594484

#make_html(html_tag('test'))
        
    
from functools import wraps

texting = 'i code with Pybites'

def add_html(fn):
    def wrapper(tag1):
        return f'{tag1} + fn() + /{tag1}'
    return wrapper

def add_another_html(fn):
    def wrapper(tag1):
        return f'{tag1} + fn() + /{tag1}'
    return wrapper

@add_another_html
def get_text2(text=texting):
    print("input text: ", text)
    return text

get_text2('strong')

#############################################

def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper

def sandwich(food="--ham--"):
    print(food)

#sandwich()
#outputs: --ham--
#sandwich = bread(ingredients(sandwich))
#sandwich()

    
    







