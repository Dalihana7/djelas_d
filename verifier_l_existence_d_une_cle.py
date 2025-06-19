'''
commentaire
'''


__author__ = "djelas_d"


def key_exists(d: dict, key):
    '''
    commentaire
    '''
    if key in d:
        return True
    else:
        return False

# print(key_exists({"a": 1}, "a"))  # True
# print(key_exists({"a": 1}, "b"))  # False
