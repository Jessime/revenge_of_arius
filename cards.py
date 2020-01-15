import pygame

class Unit(pygame.sprite.Sprite):
    def __init__(self, option_number, image, card_info_list):
        self.health = card_info_list[option_number][0]
        self.damage = card_info_list[option_number][1]
        self.speed = card_info_list[option_number][2]
        self.ice_resistance = card_info_list[option_number][3]
        self.fire_resistance = card_info_list[option_number][4]
        self.lightning_resistance = card_info_list[option_number][5]
        self.cost = card_info_list[option_number][6]
        self.x = card_info_list[option_number][7]
        self.y = card_info_list[option_number][8]
        self.pix_x = (card_info_list[option_number][9]) 
        self.pix_y = card_info_list[option_number][10]
        self.p_designation = card_info_list[option_number][11]
        self.image = image
        self.name = card_info_list[option_number][12]
        self.spell_list = []
        self.c_i_l = card_info_list
        self.casting = False
        
    def move_card1(self, card_list, grid):
        for i in range(self.speed):
            blocking = 0
            for card in card_list:
                if (card.x == self.x + 1 and
                    card.y == self.y and
                    isinstance(card, Spell) != True and 
                    self.p_designation != card.p_designation or
                    self.x == 14):
                    blocking += 1
            if blocking == 0:        
                self.pix_x += 62
                self.x += 1
                self.x, self.y = grid[self.y][self.x].add_card(self)
                grid[self.y][self.x-1].remove_card(self)
            
    def move_card2(self, card_list, grid):
        for i in range(self.speed):
            blocking = 0
            for card in card_list:
                if (card.x == self.x - 1 and
                    card.y == self.y and
                    isinstance(card, Spell) != True and 
                    self.p_designation != card.p_designation or
                    self.x == 1):
                    blocking += 1
            if blocking == 0:        
                self.pix_x -= 62
                self.x -= 1
                self.x, self.y = grid[self.y][self.x].add_card(self)
                grid[self.y][self.x+1].remove_card(self)

    def draw_card(self):
        self.pix_x += (self.x * 62) 
        self.pix_y += (self.y * 54)

    def draw_popup_card(self, screen, corner, card_width):
        self.pix_x = corner[0]+card_width 
        self.pix_y = corner[1]
        screen.blit(self.image, [self.pix_x, self.pix_y])
    
    def pop_spells(self, card_pics):
        height = 0
        counter = 0
        self.spell_list.append(Spell(3, card_pics[3], self.c_i_l)) 
        self.spell_list.append(Spell(4, card_pics[4], self.c_i_l))
        self.spell_list.append(Spell(5, card_pics[5], self.c_i_l))
        for card in self.spell_list:
            if self.y <= 3:
                height += 54
            elif self.y > 3:
                height -= 54
            card.pix_x = self.pix_x
            card.pix_y = self.pix_y + height
            card.p_designation = self.p_designation
            if card.p_designation == 1:
                card.image = card_pics[counter + 3]
            if card.p_designation == 2:
                card.image = card_pics[counter + 15]
            counter += 1

#Displays the red cards for placing spells in the proper location
    def add_spell(self, grid, screen):
        info_card5 = pygame.image.load("info_card5.png")
        for i in range(8):
            for j in range(16):
                if self.p_designation == 1 and self.name == "santa":
                    if ((grid[i][j].x-1 <= self.x <= grid[i][j].x+1 and grid[i][j].y-1 == self.y) or
                         (grid[i][j].x-1 <= self.x <= grid[i][j].x+1 and grid[i][j].y+1 == self.y) or
                         (grid[i][j].x-1 == self.x and grid[i][j].y == self.y)):
                        screen.blit(info_card5, [grid[i][j].pix_x, grid[i][j].pix_y])
                elif self.p_designation == 2 and self.name == "santa":
                    if ((grid[i][j].x-1 <= self.x <= grid[i][j].x+1 and grid[i][j].y-1 == self.y) or
                         (grid[i][j].x-1 <= self.x <= grid[i][j].x+1 and grid[i][j].y+1 == self.y) or
                         (grid[i][j].x+1 == self.x and grid[i][j].y == self.y)):
                        screen.blit(info_card5, [grid[i][j].pix_x, grid[i][j].pix_y])
                elif self.p_designation == 1 and self.name == "reindeer":
                    if ((grid[i][j].x-2 == self.x and grid[i][j].y-2 == self.y) or
                         (grid[i][j].x-2 == self.x and grid[i][j].y+2 == self.y) or
                         (grid[i][j].x-1 == self.x and grid[i][j].y == self.y)):
                        screen.blit(info_card5, [grid[i][j].pix_x, grid[i][j].pix_y])
                elif self.p_designation == 2 and self.name == "reindeer":
                    if ((grid[i][j].x+2 == self.x and grid[i][j].y-2 == self.y) or
                         (grid[i][j].x+2 == self.x and grid[i][j].y+2 == self.y) or
                         (grid[i][j].x+1 == self.x and grid[i][j].y == self.y)):
                        screen.blit(info_card5, [grid[i][j].pix_x, grid[i][j].pix_y])
                elif self.p_designation == 1 and self.name == "elf":
                    if ((grid[i][j].x == self.x and grid[i][j].y-1 >= self.y >= grid[i][j].y-2) or
                         (grid[i][j].x == self.x and grid[i][j].y+1 <= self.y <= grid[i][j].y+2) or
                         (grid[i][j].x-1 == self.x and grid[i][j].y == self.y)):
                        screen.blit(info_card5, [grid[i][j].pix_x, grid[i][j].pix_y])
                elif self.p_designation == 2 and self.name == "elf":
                    if ((grid[i][j].x == self.x and grid[i][j].y-1 >= self.y >= grid[i][j].y-2) or
                         (grid[i][j].x == self.x and grid[i][j].y+1 <= self.y <= grid[i][j].y+2) or
                         (grid[i][j].x+1 == self.x and grid[i][j].y == self.y)):
                        screen.blit(info_card5, [grid[i][j].pix_x, grid[i][j].pix_y])            
                
        
class Spell(pygame.sprite.Sprite):
    def __init__(self, option_number, image, card_info_list):
        self.elf_caster = card_info_list[option_number][0]
        self.santa_caster = card_info_list[option_number][1]
        self.reindeer_caster = card_info_list[option_number][2]
        self.duration = card_info_list[option_number][3]
        self.cost = card_info_list[option_number][4]
        self.x = card_info_list[option_number][5]
        self.y = card_info_list[option_number][6]
        self.pix_x = card_info_list[option_number][7]
        self.pix_y = card_info_list[option_number][8]
        self.p_designation = card_info_list[option_number][9]
        self.image = image
        self.name = card_info_list[option_number][10]
        self.damage = int

    def draw_card(self):
        self.pix_x += (self.x * 62) 
        self.pix_y += (self.y * 54)

    def check_duration(self):
        if self.duration >= 1:
            self.duration -= 1

    def casting_damage(self, action):
        if action == 2.1 or action == 6.1:
            self.damage = self.santa_caster
        if action == 2.2 or action == 6.2:
            self.damage = self.reindeer_caster
        if action == 2.3 or action == 6.3:
            self.damage = self.elf_caster

class Defense(pygame.sprite.Sprite):
    def __init__(self, option_number, image, card_info_list):
        self.health = card_info_list[option_number][0]
        self.damage = card_info_list[option_number][1]
        self.cost = card_info_list[option_number][2]
        self.x = card_info_list[option_number][3]
        self.y = card_info_list[option_number][4]
        self.pix_x = card_info_list[option_number][5]
        self.pix_y = card_info_list[option_number][6]
        self.p_designation = card_info_list[option_number][7]       
        self.image = image
        self.name = card_info_list[option_number][8]

    def draw_card(self):
        self.pix_x += (self.x * 62) 
        self.pix_y += (self.y * 54)        
               
class Production(pygame.sprite.Sprite):
    def __init__(self, option_number,  image, card_info_list):
        self.production_type = card_info_list[option_number][0]
        self.health =  card_info_list[option_number][1]
        self.pro_rate =  card_info_list[option_number][2]
        self.cost =  card_info_list[option_number][3]
        self.x = card_info_list[option_number][4]
        self.y = card_info_list[option_number][5]
        self.pix_x = card_info_list[option_number][6]
        self.pix_y = card_info_list[option_number][7]
        self.p_designation = card_info_list[option_number][8]        
        self.image =  image
        self.name =  card_info_list[option_number][9]
        self.damage = 0
     
    def draw_card(self):
        self.pix_x += (self.x * 62) 
        self.pix_y += (self.y * 54)
