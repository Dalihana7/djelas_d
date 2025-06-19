'''
commentaire
'''


__author__ = "djelas_d"


def filter_even(numbers: list):
    '''
    commentaire
    '''
    pairs = list(filter(lambda x: x % 2 == 0, numbers))
    return pairs


# print(filter_even([1, 2, 3, 4]))  # [2, 4]
