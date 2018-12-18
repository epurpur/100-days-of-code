# Decorators

import time
from functools import wraps

def my_logger(original_function):
    import logging
    print("Initializing logging")
    logging.basicConfig(filename='Logfile.log', level = logging.INFO)
    
    @wraps(original_function)              #preserves information from original_function
    def wrapper(*args, **kwargs):
        print("wrapping...")
        logging.info(f'Ran with args: {args} and kwargs {kwargs}' )        #this is being written to the log file
        
        return original_function(*args, **kwargs)
    
    return wrapper
    

def my_timer(original_function):
    import time
    
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        time_begin = time.time()
        result = original_function(*args, **kwargs) #running original_function and setting it equal to result
        time_end = time.time() - time_begin         #we want to get end time before returning result
        print(f"{original_function.__name__} ran in {time_end} seconds")
        return result
    
    return wrapper          #return un-executed wrapper which allows this functionality to be applied to original_function

@my_logger
@my_timer
def display_info(arg1, arg2):
    time.sleep(1)
    print(f'display function ran with arguments {arg1} and {arg2}')
    
display_info(100, 2)
    


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:39:48 2018

@author: ep9k
"""

