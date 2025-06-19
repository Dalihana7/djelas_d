'''
creation_d_une_liste
'''


__author__ = "djelas_d"


def create_list(n: int) :
    '''
    creation_d_une_liste
    '''
    result=[]
    for i in range(1, n + 1):
        result.append(i) #  ajout au tableau vide au dessus (result) sans ecraser la derniere valeur avec append()
    return result

print(create_list(5))  # [1, 2, 3, 4, 5] 


# range(1,6)
# il va boucler entre 1 et 6