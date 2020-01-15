import pygame, time

def timer(countdown, start_time, screen):
    white = [255, 255, 255]
    font = pygame.font.Font(None, 30)
    now_time = time.time()
    display_timer = int(countdown + start_time - now_time)    
    timer_text = font.render("Timer",True,white)
    timer_text2 = font.render(str(display_timer),True,white)
    screen.blit(timer_text, [835, 575])
    screen.blit(timer_text2, [850, 575+35])
    return display_timer
