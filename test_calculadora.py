import unittest
import sys
from Calculadora import CalculadoraUnidades

# Flag para suprimir prints durante tests
sys._called_from_test = True

class TestCalculadoraUnidades(unittest.TestCase):
    def test_metros_a_centimetros(self):
        self.assertEqual(CalculadoraUnidades.metros_a_centimetros(2), 200)
        self.assertEqual(CalculadoraUnidades.metros_a_centimetros("2"), 200)
        self.assertIsNone(CalculadoraUnidades.metros_a_centimetros("abc"))
        self.assertIsNone(CalculadoraUnidades.metros_a_centimetros(None))

    def test_millas_a_kilometros(self):
        self.assertAlmostEqual(CalculadoraUnidades.millas_a_kilometros(1), 1.60934)
        self.assertAlmostEqual(CalculadoraUnidades.millas_a_kilometros("2"), 3.21868)
        self.assertIsNone(CalculadoraUnidades.millas_a_kilometros("xyz"))
        self.assertIsNone(CalculadoraUnidades.millas_a_kilometros(None))

    def test_centimetros_a_metros(self):
        self.assertEqual(CalculadoraUnidades.centimetros_a_metros(200), 2)
        self.assertEqual(CalculadoraUnidades.centimetros_a_metros("100"), 1)
        self.assertIsNone(CalculadoraUnidades.centimetros_a_metros("abc"))
        self.assertIsNone(CalculadoraUnidades.centimetros_a_metros(None))

    def test_metros_a_milimetros(self):
        self.assertEqual(CalculadoraUnidades.metros_a_milimetros(2), 2000)
        self.assertEqual(CalculadoraUnidades.metros_a_milimetros("3"), 3000)
        self.assertIsNone(CalculadoraUnidades.metros_a_milimetros("abc"))
        self.assertIsNone(CalculadoraUnidades.metros_a_milimetros(None))

    def test_milimetros_a_metros(self):
        self.assertEqual(CalculadoraUnidades.milimetros_a_metros(2000), 2)
        self.assertEqual(CalculadoraUnidades.milimetros_a_metros("1000"), 1)
        self.assertIsNone(CalculadoraUnidades.milimetros_a_metros("abc"))
        self.assertIsNone(CalculadoraUnidades.milimetros_a_metros(None))

    def test_metros_a_kilometros(self):
        self.assertEqual(CalculadoraUnidades.metros_a_kilometros(1000), 1)
        self.assertEqual(CalculadoraUnidades.metros_a_kilometros("2000"), 2)
        self.assertIsNone(CalculadoraUnidades.metros_a_kilometros("abc"))
        self.assertIsNone(CalculadoraUnidades.metros_a_kilometros(None))

    def test_kilometros_a_metros(self):
        self.assertEqual(CalculadoraUnidades.kilometros_a_metros(2), 2000)
        self.assertEqual(CalculadoraUnidades.kilometros_a_metros("3"), 3000)
        self.assertIsNone(CalculadoraUnidades.kilometros_a_metros("abc"))
        self.assertIsNone(CalculadoraUnidades.kilometros_a_metros(None))

    def test_kilometros_a_millas(self):
        self.assertAlmostEqual(CalculadoraUnidades.kilometros_a_millas(1.60934), 1, places=5)
        self.assertAlmostEqual(CalculadoraUnidades.kilometros_a_millas("3.21868"), 2, places=5)
        self.assertIsNone(CalculadoraUnidades.kilometros_a_millas("abc"))
        self.assertIsNone(CalculadoraUnidades.kilometros_a_millas(None))

if __name__ == "__main__":
    unittest.main()
