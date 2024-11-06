class Cctv():
    '''监控类父类'''
    def __init__(self) -> None:
        """监控默认启动项"""


class CctvOutside(Cctv):
    '''监控类外部'''
    def __init__(self) -> None:
        super().__init__()

    def take_video(self):
        print(f"拍摄监控")


class CctvInside(Cctv):
    """监控类内部"""
    def __init__(self) -> None:
        super().__init__()

    def check(self):
        """查看监控功能"""
        print(f"查看监控")

    def forward(self):
        """转发监控功能"""
        print(f"转发监控")


class App():
    """移动端父类"""
    def __init__(self) -> None:
        pass


class AppOutside(App):
    """移动端内部系统"""
    def __init__(self) -> None:
        super().__init__()

    def check(self):
        """监控功能"""
        print(f"查看监控")

    def call(self):
        """与外部系统通话"""
        print(f"与外部系统通话")


class AppInside(App):
    """移动端内部系统"""
    def __init__(self) -> None:
        super().__init__()

    def call(self):
        """与内部通话"""
        print(f"与内部系统通话")


if __name__ == "__main__":
    """外部监控系统启动"""
    cctv_outside = CctvOutside()
    cctv_outside.take_video()

    """内部启动"""
    cctv_inside = CctvInside()
    cctv_inside.check()
    cctv_inside.forward()

    """app"""
    