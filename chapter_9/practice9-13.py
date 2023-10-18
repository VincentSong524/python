from random import randint

class Die:
    """骰子"""

    def __init__(self, sides = 6) -> None:
        """初始化一个默认六面的骰子"""
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))


ten = Die(10)
ten.roll_die()

twenty = Die(20)
twenty.roll_die()