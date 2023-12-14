#https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
#Solution:

def create_phone_number(n):
    n.insert(0, "(")
    n.insert(4, ")")
    n.insert(5, " ")
    n.insert(9, "-")
    string = ''.join([str(item) for item in n])
    return string