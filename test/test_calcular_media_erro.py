from boletim.calculos import calcular_media
import pytest


def test_lista_vazia():
    with pytest.raises(ValueError, match="A lista de notas não pode estar vazia"):
        calcular_media([])

def test_string():
    with pytest.raises(TypeError, match="As notas devem ser uma lista numérica"):
        calcular_media("OITO")

def test_notas_nao_numericas():
    with pytest.raises(TypeError, match="As notas devem ser uma lista numérica"):
        calcular_media(["um","oito"])

def test_notas_numerica_nao_numerica():
    with pytest.raises(TypeError, match="As notas devem ser uma lista numérica"):
        calcular_media([10,"cinco",4])

def test_maiores_10():
    with pytest.raises(ValueError):
        calcular_media([11, 100])

def test_nota_negativa():
    with pytest.raises(ValueError):
        calcular_media([-11,-100])
    
def test_notas_numerica_nao_numerica():
    with pytest.raises(ValueError, match="A lista de notas não pode estar vazia"):
        calcular_media(8)

