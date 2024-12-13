# circle.py

from math import pi 

def area(r):
    if type(r) not in [int,float]:
        raise ValueError("can only handle int, float datatype.")
    if r<0:
        raise ValueError("neg value cannot be processed")
    return pi * (r * r)