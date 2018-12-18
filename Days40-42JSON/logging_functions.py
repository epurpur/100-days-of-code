from functools import wraps      #allows you to preserve the information from the original function


def my_logger(original_function, filename = "WeatherAppLogfile.log"):  
    import logbook
    import sys
    level = logbook.TRACE

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = f"Logging Initialized. level: {level}, mode: {'stdout mode' if not filename else 'file mode: ' + filename}"
    logger = logbook.Logger("Startup level")
    logger.notice(msg)


    @wraps(original_function)               #preserves information from original function. Decorate wrappers with wraps
    def wrapper(*args, **kwargs):
        wrap_logger = logbook.Logger("Wrapper Level")
        wrap_logger.trace(f'Staring logging for function {original_function.__name__}')     #returns name of function
            
        result = original_function(*args, **kwargs)    
        
        wrap_logger.trace(f'Finished logging for function {original_function.__name__}')

        
        return result

    return wrapper