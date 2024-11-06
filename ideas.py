def cctv():
    def cctv_outside():
        def take_video():
            print(f"监控端拍摄视频")
    
    def cctv_inside():
        def check():
            print(f"监控端查看监控")
        
        def forward():
            print(f"转发监控至移动端并主动弹出")


def app(choose):
    def app_outside():
        def check():
            print(f"移动端查看监控")

        def tall():
            print(f"移动端外部通话")
    
    def app_inside():
        def tall():
            print(f"移动端内部通话")



if __name__ == "__main__":
    while True:
        print(f"移动端功能展示：\n[1]查看监控|[2]外部通话|[3]内部通话|[0]结束展示|")
        choose = input("%d")
