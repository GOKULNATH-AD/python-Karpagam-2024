import unittest
import circle as ca
import math

class CircleTest(unittest.TestCase):
    def test_validateIntType(self):
        self.assertEqual(ca.area(2), math.pi*(2*2))
        self.assertEqual(ca.area(4), math.pi*(4*4))
        self.assertEqual(ca.area(3), math.pi*(3*3))

    def test_validateFloatType(self):
        self.assertEqual(ca.area(2.3), math.pi*(2.3*2.3))
        self.assertEqual(ca.area(4.3), math.pi*(4.3*4.3))
        self.assertEqual(ca.area(3.2), math.pi*(3.2*3.2))

    def test_handleInvalidTypes(self):
        self.assertRaises(ValueError, ca.area, -2)
        self.assertRaises(ValueError, ca.area, "2")
        self.assertRaises(ValueError, ca.area, True)

unittest.main()
