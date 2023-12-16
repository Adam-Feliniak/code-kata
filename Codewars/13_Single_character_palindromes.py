#https://www.codewars.com/kata/5a2c22271f7f709eaa0005d3/train/python
#Solution from Codewars:
def solve(s):
    if s == s[::-1]:
        return 'OK'
    for i in range(len(s)):
        if s[:i] + s[i+1:] == (s[:i] + s[i+1:])[::-1]:
            return 'remove one'
    return 'not possible'

# My try
def solve(s):
    if len(s) % 2 == 0:
        centre = len(s) // 2
        first = list(s[:centre])
        second = list(s[centre:])
        second.reverse()
        if first == second:
            return "OK"
        else:
            return "not possible"
    else:
        for i in range(len(s)):
            if is_palindrome_after_removal(s, i):
                return "remove one"
        return "not possible"

def is_palindrome_after_removal(s, index):
    modified_string = s[:index] + s[inde x +1:]
    return modified_string == modified_string[::-1]