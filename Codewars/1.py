#https://www.codewars.com/kata/524f5125ad9c12894e00003f
#solution

def remainder(a,b):
    bigger = max(a,b)
    smaller = min(a,b)
    if smaller == 0:
        return None
    else:
        result = bigger % smaller
        return result