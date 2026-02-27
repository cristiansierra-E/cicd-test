from  calculadora import Calculadora
def test_add():
    calc = Calculadora()
    assert calc.add(2, 3) == 5
    
def test_multiplicacion():
    calc = Calculadora()
    assert calc.multiplicacion(2, 3) == 6
    
def test_resta():
    calc = Calculadora()
    assert calc.resta(5, 2) == 3    