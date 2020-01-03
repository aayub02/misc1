import unittest
import shapes.triangle as triangle

class AATest(unittest.TestCase):

    def setUp(self):
<<<<<<< HEAD
=======
        'IT IS RUNNING!!!!'
>>>>>>> fb9765c3ce0f1958c94fe4bde80b650fc1b6b732
        self.t1 = triangle.Triangle([45, 45, 90], 'whyname')

    def test_validate_num(self):
        self.assertRaises(ValueError, triangle.Triangle.validate_num, 1)
        self.assertRaises(ValueError, triangle.Triangle.validate_num, (1))
        self.assertRaises(ValueError, triangle.Triangle.validate_num, {1: 'a'})
        self.assertRaises(ValueError, triangle.Triangle.validate_num)
        self.assertRaises(ValueError, triangle.Triangle.validate_num, ['', 1])
        self.assertRaises(ValueError, triangle.Triangle.validate_num, ['s', 1])
        self.assertRaises(ValueError, triangle.Triangle.validate_num, [2, -1])
        self.assertRaises(ValueError, triangle.Triangle.validate_num, [45, 45, 45, 45])
        self.assertRaises(ValueError, triangle.Triangle.validate_num, [90, 90])
        self.assertRaises(ValueError, triangle.Triangle.validate_num, [45, 44.5, 90])

    def test_validate_name(self):
        self.assertRaises(ValueError, setattr, self.t1, 'name', 1)

    def test_angles(self):
        self.assertLessEqual(abs(sum(self.t1.angles)-180), 0.1)


if __name__ == '__main__':
    unittest.main()
