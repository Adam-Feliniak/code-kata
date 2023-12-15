#https://www.codewars.com/kata/56fc55cd1f5a93d68a001d4e/train/python
#Solution:

def stairs_in_20(stairs):
    stairs_sum = 0
    for day in stairs:
        for sum in day:
            stairs_sum += sum
    return stairs_sum*20