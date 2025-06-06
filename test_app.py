"""
Testes para o módulo app.py.
"""

from app import soma

def test_soma():
    """
    Testa a função soma, verificando se a soma de 7 e 10 é 17.
    """
    assert soma(7, 10) == 17
