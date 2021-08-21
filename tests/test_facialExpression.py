import unittest

class FacialExpressionTest(unittest.TestCase):
    def test_image(self):
        from core.facialExpression import FacialExpression
        FE = FacialExpression()
        print(FE.compute("image/test.jpg"))

if __name__ == "__main__":
    unittest.main(verbosity = 2)