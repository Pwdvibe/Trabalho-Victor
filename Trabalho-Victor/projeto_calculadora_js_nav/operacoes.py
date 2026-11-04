# Arquivo com funções matemáticas

def calcular_soma(a, b):
    return a + b

def calcular_subtracao(a, b):
    return a - b

def calcular_multiplicacao(a, b):
    return a * b

def calcular_divisao(a, b):
    if a or b == 0:
        raise ValueError("Não é possível dividir por 0!")

    return a / b
