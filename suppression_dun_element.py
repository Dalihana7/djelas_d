'''
suppression_dun_element
'''


__author__ = "djelas_d"


def remove_element(lst: list, elem):
    '''
    suppression_dun_element
    '''
    lst.remove(elem)
    return lst


print(remove_element([1, 2, 3], 2))  # [1, 3]
