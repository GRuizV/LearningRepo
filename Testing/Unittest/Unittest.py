import unittest



# Base Class
class Rectangle:

    def __init__(self, width, height) -> None:

        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


# First Testing
# class TestGetAreaRectangle(unittest.TestCase):

    # # Testing common cases
    # def test_normal_case(self):

    #     rectangle = Rectangle(2, 3)
    #     self.assertEqual(rectangle.get_area(), 6, "incorrect area")


    # #Test expected to fail
    # def test_negative_case(self): 
    #     """expect -1 as output to denote error when looking at negative area"""
    #     rectangle = Rectangle(-1, 2)
    #     self.assertEqual(rectangle.get_area(), -1, "incorrect area")


    # def test_geq(self):
    #     """test if value is greter than or equal to a particular target"""
    #     rectangle = Rectangle(-1, 2)
    #     self.assertGreaterEqual(rectangle.get_area(), -3)


    # def test_assert_raises(self):
    #     """using assertRaises to detect if an expected error is raised when running a particular block of code"""
    #     with self.assertRaises(ZeroDivisionError):
    #         a = 1/0


    # # working with fixtures
    # def setUp(self):
    #     self.rectangle = Rectangle(0, 0)

    
    # def test_normal_case_w_fixture(self):

    #     self.rectangle.set_width(2)
    #     self.rectangle.set_height(3)

    #     self.assertEqual(self.rectangle.get_area(), 6, 'Incorrect Area')

    # def test_negative_case_w_fixture(self):

    #     self.rectangle.set_width(-1)
    #     self.rectangle.set_height(2)
        
    #     self.assertEqual(self.rectangle.get_area(), -2, 'Incorrect Area')
    


class TestGetAreaRectangleWithSetUp(unittest.TestCase):

    """
    This class is made to force run this setup only once, 
    diffent from the setUp func in the prior class, 
    which runs the setUp each time a test is run.
    """

    @classmethod
    def setUpClass(self):
        self.rectangle = Rectangle(0, 0)
    

    def test_normal_case(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")

    def test_geq(self):
        """test if value is greter than or equal to a particular target"""
        rectangle = Rectangle(-1, 2)
        self.assertGreaterEqual(rectangle.get_area(), -3)

    def test_assert_raises(self):
        """using assertRaises to detect if an expected error is raised when running a particular block of code"""
        with self.assertRaises(ZeroDivisionError):
            a = 1/0


# This line is a suite that will tests from the class that were just defined
calculate_area_suite = unittest.TestLoader().loadTestsFromTestCase(TestGetAreaRectangleWithSetUp)

runner = unittest.TextTestRunner()
runner.run(calculate_area_suite)




# Safeguard conditional
if __name__ == "__main__":

    unittest.main()