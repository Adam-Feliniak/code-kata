#https://www.codewars.com/kata/563cf89eb4747c5fb100001b/python
#solution

def remove_smallest(numbers):
    if not numbers:
        return []
    else:
        numbers_copy = list(numbers)
        numbers_copy.remove(min(numbers_copy))
        return numbers_copy