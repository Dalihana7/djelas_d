'''
commentaire
'''


__author__ = "djelas_d"


def remove_key(d: dict, key):
    '''
    commentaire
    '''
    if key in d:
        del d[key]
    return d


# print(remove_key({"a": 1, "b": 2}, "a"))  # {"b": 2}
