#https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python
#Solution:

def summation(num):
    for i in range(1,num+1):
        my_range = range(1,i+1)
        my_list = list(my_range)
    return sum(my_list)