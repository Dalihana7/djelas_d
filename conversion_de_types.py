'''
conversion_de_types
'''

__author__ = "djelas_d"


def convert_type(value):
    '''
    conversion_de_types
    '''
    # Si la valeur est une chaîne de caractères
    if isinstance(value, str):
        return int(value)  # Convertir la chaîne en entier
    # Si la valeur est un entier
    elif isinstance(value, int):
        return str(value)  # Convertir l'entier en chaîne de caractères
    else:
        raise TypeError("La valeur doit être soit une chaîne soit un entier.")
