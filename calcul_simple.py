'''
calcul_simple
'''

__author__ = "djelas_d"


def basic_operations(a: int, b: int) -> tuple:


    addition = a + b
    soustraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else 'Division par zéro'

    return (addition, soustraction, multiplication, division)
