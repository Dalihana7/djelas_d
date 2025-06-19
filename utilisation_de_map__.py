'''
commentaire
'''


__author__ = "djelas_d"


def to_upper(words: list):
    '''
    commentaire
    '''
    mots_majuscule = list(map(lambda x: x.upper(), words))
    return mots_majuscule

# print(to_upper(["hello", "world"]))  # ["HELLO", "WORLD"]
