import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ship, ai_settings, screen, bullets):
    """ 响应按键 """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """ 响应松开 """
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False


def check_events(ai_settings, screen, ship, aliens, bullets, stats,
                 play_button, scoreboard):
    """ 响应按键和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, ship, aliens, bullets,
                              stats, play_button, mouse_x, mouse_y, scoreboard)


def check_play_button(ai_settings, screen, ship, aliens, bullets, stats,
                      play_button, mouse_x, mouse_y, scoreboard):
    """ 点击play按钮开始 """
    if play_button.rect.collidepoint(mouse_x,
                                     mouse_y) and not stats.game_active:
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置速度
        ai_settings.initialize_dynamic_settings()

        # 重置统计信息
        scoreboard.prep_score()
        scoreboard.prep_high_score()
        scoreboard.prep_level()
        scoreboard.prep_ships()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 清空alien and bullets
        aliens.empty()
        bullets.empty()

        # 创建新舰队，居中ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, ship, aliens, bullets, stats,
                  play_button, scoreboard):
    """ 更新屏幕上的图像，并切换到新屏幕 """
    # 每次循环时都重回屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    # 显示得分
    scoreboard.show_score()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    if not stats.game_active:
        play_button.draw_button()

    # 让最近的绘制屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, bullets, aliens, screen, ship, stats,
                   scoreboard):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_alien_bullet_collisions(ai_settings, screen, ship, aliens, bullets,
                                  stats, scoreboard)


def check_alien_bullet_collisions(ai_settings, screen, ship, aliens, bullets,
                                  stats, scoreboard):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            scoreboard.prep_score()
        check_high_score(stats, scoreboard)
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increse_speed()

        # 提高等级
        stats.level += 1
        scoreboard.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_alien_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / alien_width / 2)
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.y = alien.rect.height + 2 * row_number * alien.rect.height
    alien.rect.y = alien.y
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """ 计算屏幕可容纳多少行alien """
    available_space_y = (
        ai_settings.screen_height - 3 * alien_height - ship_height)
    number_rows = int(available_space_y / 2 / alien_height)
    return number_rows


def update_aliens(ai_settings, screen, ship, stats, bullets, aliens,
                  scoreboard):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测alien 和 ship 之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        print('Ship hit!!!')
        ship_hit(stats, aliens, bullets, ai_settings, screen, ship, scoreboard)
    check_alien_bottom(ai_settings, screen, ship, aliens, bullets, stats,
                       scoreboard)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if (alien.check_edges()):
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(stats, aliens, bullets, ai_settings, screen, ship, scoreboard):
    """ 相应ship 和 alien 相撞 """
    if (stats.ships_left > 0):
        stats.ships_left -= 1
        # 更新ship 计数板
        scoreboard.prep_ships()
        print('ship left ' + str(stats.ships_left))
        sleep(0.5)
        aliens.empty()
        bullets.empty()

        # 创建新的 舰队
        create_fleet(ai_settings, screen, ship, aliens)
        # 重置ship位置
        ship.center_ship()
    else:
        print('game over!!')
        stats.game_active = False
        # 显示光标
        pygame.mouse.set_visible(True)


def check_alien_bottom(ai_settings, screen, ship, aliens, bullets, stats,
                       scoreboard):
    """ 处理alien 到达屏幕底部 """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if (alien.rect.bottom >= screen_rect.height):
            print('alien arrived bottom!!')
            ship_hit(stats, aliens, bullets, ai_settings, screen, ship,
                     scoreboard)
            break


def check_high_score(stats, scoreboard):
    """ 检查高分 """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()