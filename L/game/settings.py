class Settings():
    """ 存储所有设置的类 """

    def __init__(self):
        """ 初始化游戏设置 """
        # 设置屏幕
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 50

        self.bullet_speed_factor = 80
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5