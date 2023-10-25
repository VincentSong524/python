import unittest
from practice11_3 import Employee

class TestEmployee(unittest.TestCase):
    """测试 Empoyee 类"""

    def setUp(self):
        """初始化需要测试的类"""
        self.employee = Employee('henry', 'morgan', 10000)

    def test_give_default_raise(self):
        """测试使用默认值的方法"""
        self.employee.give_raise()
        self.assertEqual(15000, self.employee.annul_salary)

    def test_give_custom_raise(self):
        """测试不使用默认值的方法"""
        self.employee.give_raise(10000)
        self.assertEqual(20000, self.employee.annul_salary)


if __name__ == '__main__':
    unittest.main()