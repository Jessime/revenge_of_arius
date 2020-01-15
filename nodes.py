import pygame, random, cards, buttons

# Fog of war images
fog_image = pygame.image.load("fog_of_war.png")
fog_image2 = pygame.image.load("fog_of_war2.png")
fog_image3 = pygame.image.load("fog_of_war3.png")
fog_image4 = pygame.image.load("fog_of_war4.png")
# Pop_up images
popup_bg = pygame.image.load("snowfall_background3.png")
info_card4 = pygame.image.load("info_card4.png")
class Node:
    def __init__(self, x, y):
        self.occupants_list = []
        self.x = x
        self.y = y
        self.pix_x = 155 + (self.x * 62)
        self.pix_y =  122 + (self.y * 54)
        self.fogged = False
        self.pic_num = random.randint(1,4)
        self.pop_set = 0
    def remove_card(self, Unit):
        self.occupants_list.remove(Unit)
    def add_card(self, Unit):
        self.occupants_list.append(Unit)
        return self.x, self.y

    def pop_up(self, screen):
        green = [0, 176, 80]
        if len(self.occupants_list) <= 8:
            width = len(self.occupants_list) * 62
        else:
            width = 8 *62
        card_width = 0
        # For the top left quadrant
        if self.x <= 7 and self.y <= 3:
            corner = [self.pix_x , self.pix_y + 54] # Define top left corner of popup
            screen.blit(popup_bg, corner, [0, 0, width, 54*4]) # Blit background
            screen.blit(info_card4, [self.pix_x, self.pix_y]) # Cover the node with card
            pygame.draw.rect(screen, green, [corner[0]-3, corner[1]-3, width+3, (54*4)+3], 3) # Outline
            if len(self.occupants_list) <= 8:
                for card in self.occupants_list: # Display all cards in node
                    card.pix_x = corner[0] + card_width
                    card.pix_y = corner[1]
                    screen.blit(card.image, [card.pix_x, card.pix_y])
                    card_width += 62
            else:
                #screen.blit(buttons.next_btn.visible, [corner[0] + width - 62, corner[1] + 54*4])
                #screen.blit(buttons.back_btn.visible, [corner[0] , corner[1] + 54*4])
                for card in self.occupants_list[:8]:
                    card.pix_x = corner[0] + card_width
                    card.pix_y = corner[1]
                    screen.blit(card.image, [card.pix_x, card.pix_y])
                    card_width += 62 

        # For the top right quadrant
        elif self.x > 7 and self.y <= 3:
            if len(self.occupants_list) <= 8:
                corner = [self.pix_x - ((len(self.occupants_list) - 1)*62), self.pix_y + 54]
            else:
                corner = [self.pix_x - (7*62), self.pix_y + 54]
            screen.blit(popup_bg, corner, [0, 0, width, 54*4])
            screen.blit(info_card4, [self.pix_x, self.pix_y])
            pygame.draw.rect(screen, green, [corner[0]-3, corner[1]-3, width+3, (54*4)+3], 3)
            if len(self.occupants_list) <= 8:
                for card in self.occupants_list:
                    card.pix_x = corner[0] + card_width
                    card.pix_y = corner[1]
                    screen.blit(card.image, [card.pix_x, card.pix_y])
                    card_width += 62
            else:
                #screen.blit(buttons.next_btn.visible, [corner[0] + width - 62, corner[1] + 54*4])
                #screen.blit(buttons.back_btn.visible, [corner[0] , corner[1] + 54*4])
                for card in self.occupants_list[:8]:
                    card.pix_x = corner[0] + card_width
                    card.pix_y = corner[1]
                    screen.blit(card.image, [card.pix_x, card.pix_y])
                    card_width += 62 
             
        # For the bottom left quadrant
        elif self.x <= 7 and self.y > 3:
            corner = [self.pix_x, self.pix_y - (54*4)]
            screen.blit(popup_bg, corner, [0, 0, width, 54*4])
            screen.blit(info_card4, [self.pix_x, self.pix_y])            
            pygame.draw.rect(screen, green, [corner[0], corner[1], width, (54*4)], 3)
            if len(self.occupants_list) <= 8:
                for card in self.occupants_list:
                    card.pix_x = corner[0] + card_width
                    card.pix_y = corner[1] + (54 *3)
                    screen.blit(card.image, [card.pix_x, card.pix_y])
                    card_width += 62
            else:
                #screen.blit(buttons.next_btn.visible, [corner[0] + width - 62, corner[1]])
                #screen.blit(buttons.back_btn.visible, [corner[0] , corner[1]])
                for card in self.occupants_list[:8]:
                    card.pix_x = corner[0] + card_width
                    card.pix_y = corner[1] + (54 *4)
                    screen.blit(card.image, [card.pix_x, card.pix_y])
                    card_width += 62  
            
       # For the bottom right quadrant
        elif self.x > 7 and self.y > 3:
            if len(self.occupants_list) <= 8:
                corner = [self.pix_x - ((len(self.occupants_list) - 1)*62), self.pix_y  - (54 *4)]
            else:
                corner = [self.pix_x - (7*62), self.pix_y  - (54 *5)]
            screen.blit(popup_bg, corner, [0, 0, width, 54*4])
            screen.blit(info_card4, [self.pix_x, self.pix_y])
            pygame.draw.rect(screen, green, [corner[0]-3, corner[1]-3, width+3, (54*4)+3], 3)
            if len(self.occupants_list) <= 8:
                for card in self.occupants_list:
                    card.pix_x = corner[0] + card_width
                    card.pix_y = corner[1] + (54 *3)
                    screen.blit(card.image, [card.pix_x, card.pix_y])
                    card_width += 62
            else:
                #screen.blit(buttons.next_btn.visible, [corner[0] + width - 62, corner[1]])
                #screen.blit(buttons.back_btn.visible, [corner[0] , corner[1]])
                for card in self.occupants_list[:8]:
                    card.pix_x = corner[0] + card_width
                    card.pix_y = corner[1] + (54 *4)
                    screen.blit(card.image, [card.pix_x, card.pix_y])
                    card_width += 62

    def close_pop(self):
        for card in self.occupants_list:
            card.pix_x = self.pix_x
            card.pix_y = self.pix_y
            if isinstance(card, cards.Unit):
                if len(card.spell_list) != 0:
                    card.spell_list = []

    def init_fog(self):
        if self.x > 3:
            self.fogged = True

    def fog_of_war(self, player_turn, card_list):
        # Check if node should be fogged durning player1's turn
        if player_turn == 1:
            if self.x > 3:
                self.fogged = True
                for card in card_list:
                    if card.p_designation == player_turn:
                        if ((self.x < 12 and
                            3 < card.x < 11 and
                            card.y <= self.y + 1 and
                            card.y >= self.y - 1) or
                            (card.x >= 11 and
                            card.y <= self.y + 1 and
                            card.y >= self.y - 1)):

                            self.fogged = False
            else:
                self.fogged = False

        # Check if node should be fogged durning player2's turn
        else:
            if self.x < 12:
                self.fogged = True
                for card in card_list:
                    if card.p_designation == player_turn:
                        if ((self.x > 3 and
                            4 < card.x < 12 and
                            card.y <= self.y + 1 and
                            card.y >= self.y - 1) or
                            (card.x <= 3 and
                            card.y <= self.y + 1 and
                            card.y >= self.y - 1)):

                            self.fogged = False
            else:
                self.fogged = False

    def show_fog(self, screen):
        if self.fogged == True:
            if self.pic_num == 1:
                screen.blit(fog_image, [self.pix_x, self.pix_y])
            elif self.pic_num == 2:
                screen.blit(fog_image2, [self.pix_x, self.pix_y])
            elif self.pic_num == 3:
                screen.blit(fog_image3, [self.pix_x, self.pix_y])
            elif self.pic_num == 4:
                screen.blit(fog_image4, [self.pix_x, self.pix_y])            

    # Sort cards in occupied list so that damage is dealt to the card with the lowest health
    def damage_sort(self, card, card_list):
        health_list = []
        for card2 in self.occupants_list:
            if isinstance(card2, cards.Spell) != True and card2.p_designation != card.p_designation:
                health_list.append(card2) #Make list of cards from occupants list that can be attacked 
        health_list.sort(key = lambda x: x.health) #Sort list based on lowest health
        if len(health_list) != 0:
            health_list[0].health -= card.damage
            if health_list[0].health <= 0: #Remove card from lists if card is killed
                self.occupants_list.remove(health_list[0])
##                for card3 in card_list:
##                    if isinstance(card3, cards.Spell) != True:
##                        print(card3.name, card3 != isinstance(card3, cards.Spell))
##                        print(card3.p_designation, card3.name, card3.health, end=" ")
##                print("")
##                for card4 in health_list:
##                    if card4 != isinstance(card4, cards.Spell):
##                        print(card4.p_designation, card4.name, card4.health, end=" ")
                card_list.remove(health_list[0])
