from logger import logging

def add(a,b):
    logging.debug("The addtion operation is taking place")
    return a + b

logging.debug("The addtion function is called")
add(10,15)