#https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
#Solution:

def generate_hashtag(s):
    if s == "":
        return False
    else:
        hash_list = list(("#" + s.title()).split(" "))
        hash = ''.join(hash_list)
        if len(hash) <= 140:
            return hash
        else:
            return False