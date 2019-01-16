class Settings():
    """ 存储所有设置的类 """

    def __init__(self):
        """ 初始化游戏设置 """
        # 设置屏幕
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship 设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # alien 设置
        self.fleet_drop_speed = 30

        # 加速幅度
        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ 初始化随游戏进行而变化的设置 """
        self.ship_speed_factor = 50
        self.bullet_speed_factor = 80
        self.alien_speed_factor = 20

        # 1 right -1 left
        self.fleet_direction = 1
        # 计分
        self.alien_points = 50

    def increse_speed(self):
        """ 提高速度 """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.speedup_scale)
