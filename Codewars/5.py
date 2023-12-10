#https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
#Solution:

def open_or_senior(data):
    results = []
    for i in data:
        if i[0] > 54 and i[1] >7 :
            results.append("Senior")
        else:
            results.append("Open")
    return results