import unittest 
import circle_area as ca
import math 

class TestCircleArea(unittest.TestCase):
    def setup(self):
        self.number = 10

    def tearDown(self):
        return super().tearDown()
    
    def test_area(self):
        # check if basic functionality of area is working...
        self.assertAlmostEqual(ca.circle_area(2), math.pi*(2*2))
        self.assertAlmostEqual(ca.circle_area(4), math.pi*(4*4))
        self.assertAlmostEqual(ca.circle_area(3), math.pi*(3*3))
        self.assertEqual

    def test_area_with_invalid_types(self):
        # check functionality of area with diff invalid datatype.
        self.assertRaises(ValueError,ca.circle_area,-2)
        self.assertRaises(ValueError,ca.circle_area,"2")
        self.assertRaises(ValueError,ca.circle_area,True)
        self.assertRaises(ValueError,ca.circle_area,False)
        self.assertRaises(ValueError,ca.circle_area,[1,2])
        self.assertRaises(ValueError,ca.circle_area,(1,2))

    def test_area_with_valid_types(self):
        # check functionality of area with diff invalid datatype.
        self.assertAlmostEqual(ca.circle_area(4), math.pi*(4*4))
        self.assertAlmostEqual(ca.circle_area(4.5), math.pi*(4.5*4.5))
        
