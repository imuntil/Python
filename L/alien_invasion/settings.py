class Settings():
    """游戏设置"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        # self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹
        # self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien
        # self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # self.fleet_direction = 1

        # 游戏加速幅度
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """ 初始化游戏中会变化的设置 """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """ 提高速度设置 """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
