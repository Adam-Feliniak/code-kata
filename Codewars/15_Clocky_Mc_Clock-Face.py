#https://www.codewars.com/kata/59752e1f064d1261cb0000ec/train/python
#Solution
import math

def what_time_is_it(angle):
    minutes = angle*2;
    H = math.floor(minutes / 60)
    M = math.floor(minutes % 60)
    if H < 1:
        return f"12:{M:02.0f}"
    if H > 12:
        return f"{H:02.0f-12}:{M:02.0f}"
    else:
        return f"{H:02.0f}:{M:02.0f}"