#https://www.codewars.com/kata/5601409514fc93442500010b/train/python
#Solution:

def better_than_average(class_points, your_points):
    class_average = sum(class_points)/len(class_points)
    if your_points > class_average:
        return True
    else:
        return False