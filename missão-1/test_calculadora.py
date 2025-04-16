import pytest
from calculadora import calculadora 

def test_soma():
    assert calculadora('soma', 2, 3) == 5
    assert calculadora('soma', -1, 1) == 0
    assert calculadora('soma', 0, 0) == 0

def test_subtração():
    assert calculadora('subtracao', 5, 3) == 2
    assert calculadora('subtracao', -1,-1) == 0
    assert calculadora('subtracao', 10, 20) == -10

def test_multiplicacao():
    assert calculadora('multiplicacao', 3, 4) == 12
    assert calculadora('multiplicacao', -2, 5) == -10
    assert calculadora('multiplicacao', 0, 10) == 0

def test_dividir():
    assert calculadora('divisao', 10, 2) == 5
    assert calculadora('divisao', 9, 3) == 3
    assert calculadora('divisao', 1, 2) == 0.5

def test_divisao_por_zero():
    with pytest.raises(ValueError, match="Divisão por zero não é permitida."):
        calculadora('divisao', 10, 0)

def test_operacao_invalida():

    with pytest.raises(ValueError, match="Operação inválida. Use 'soma', 'subtracao', 'multiplicacao' ou 'divisao'."):
        calculadora('potencia', 2, 3)
