from  calculadora import Calculadora
def test_add():
    calc = Calculadora()
    assert calc.add(2, 3) == 5
    
    def test_multiplicacion(self):
        calc = Calculadora()
        assert calc.multiplicacion(2, 3) == 6