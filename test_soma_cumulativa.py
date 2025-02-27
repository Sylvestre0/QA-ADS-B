import pytest
from soma_cumulativa import soma_cumulativa  # Importa a função do arquivo soma_cumulativa.py

# Testes para casos de sucesso
def test_soma_cumulativa_lista_positiva():
    assert soma_cumulativa([1, 2, 3, 4]) == [1, 3, 6, 10]

def test_soma_cumulativa_lista_negativa():
    assert soma_cumulativa([-1, -2, -3, -4]) == [-1, -3, -6, -10]

def test_soma_cumulativa_lista_mista():
    assert soma_cumulativa([-1, 1, -1, 1]) == [-1, 0, -1, 0]

def test_soma_cumulativa_lista_zeros():
    assert soma_cumulativa([0, 0, 0, 0]) == [0, 0, 0, 0]

def test_soma_cumulativa_lista_unica():
    assert soma_cumulativa([5]) == [5]

def test_soma_cumulativa_lista_vazia():
    assert soma_cumulativa([]) == []

# # Testes para tratamento de erros (casos de exceção)
# def test_soma_cumulativa_lista_nao_inteiros():
#     with pytest.raises(TypeError):
#         soma_cumulativa([1.5, 2.5, 3.5])  # Lista com números não inteiros

# def test_soma_cumulativa_lista_strings():
#     with pytest.raises(TypeError):
#         soma_cumulativa(["a", "b", "c"])  # Lista com strings


