class Employee:
    """接受姓名，可以增加年薪。"""

    def __init__(self, first_name, last_name, annul_salary) -> None:
        """接受姓名并存储"""
        self.first_name = first_name
        self.last_name = last_name
        self.annul_salary = annul_salary

    def give_raise(self,  rise=5000):
        """默认将年薪增加5000，也能接受其他的年薪增加量"""
        self.annul_salary += rise


if __name__ == '__main__':
    employee = Employee('henry', 'morgan', 10000)
    employee.give_raise()
    if employee.annul_salary == 15000:
        print("默认值测试正确。")
    else:
        print("默认值测试错误。")

    employee1 = Employee('harry', 'song', 15000)
    employee1.give_raise(10000)
    if employee1.annul_salary == 25000:
        print("输入值测试正确。")
    else:
        print("输入值测试错误")