import pygame
pygame.init()
font = pygame.font.Font(None, 30)
class Player:
    def __init__(self, health, gold, mana, gold_inc, name):
        self.health = health
        self.gold = gold
        self.mana = mana
        self.gold_inc = gold_inc
        self.name = name
        
    # Draw on screen statistics for each player
    def draw_stats(self, screen, health_loc, gold_loc, mana_loc, color):
        
        self.health_text1 = font.render("Health", True, color)
        self.gold_text1 = font.render("Gold", True, color)
        self.mana_text1 = font.render("Mana", True, color)
        self.health_text2 = font.render(str(self.health), True, color)
        self.gold_text2 = font.render(str(self.gold), True, color)
        self.mana_text2 = font.render(str(self.mana), True, color)
        screen.blit(self.health_text1, health_loc)
        screen.blit(self.gold_text1, gold_loc)
        screen.blit(self.mana_text1, mana_loc)
        screen.blit(self.health_text2, [health_loc[0]+7,health_loc[1]+35])
        screen.blit(self.gold_text2, [gold_loc[0],gold_loc[1]+35])
        screen.blit(self.mana_text2, [mana_loc[0]+3,mana_loc[1]+35])         


