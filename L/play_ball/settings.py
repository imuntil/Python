class Settings():
    """ 游戏设置 """
    def __init__(self):
        # 屏幕设置
        self.screen_width = 500
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ball设置
        self.ball_speed_factor = 0.2
        self.ball_width = 20
        self.ball_height = 20

        # basket设置
        self.basket_speed_factor = 0.1
        self.basket_width = 40
        self.basket_height = 25
        self.basket_color = 255, 0, 255
        
        self.changes = 3
        self.game_over = False