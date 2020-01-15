import pygame, cards, unit_stats

def tracking(screen, pick_card, card_num, card_type, player_turn, card_list):
    white = [255,255,255]
    font = pygame.font.Font(None, 30)
    pos = pygame.mouse.get_pos()
    card_num2 = int
    c_i_l =  unit_stats.unit_stats()
    
    if pick_card == True:
        x = pos[0] - 30
        y = pos[1] - 26
        if player_turn == 1:
            card_pic = pygame.image.load(card_type[card_num] + ".png")
        else:
            card_pic = pygame.image.load(card_type[card_num] + "2.png")   
        screen.blit(card_pic, [x,y])
        
    elif (312 <= pos[0] < 498) and (33 < pos[1] < 85):
        card_num2 = (pos[0]-312)// (60+2)
    elif (498 <= pos[0] < 868) and (33 < pos[1] < 85):
        card_num2 = (186+(pos[0]-312))// (60+2)
    else:
        for card in card_list:
            if isinstance(card, cards.Unit): #necessary before checking spell_list
                if card.spell_list != []:
                    for spell in card.spell_list:
                        if spell.pix_x <= pos[0] <= spell.pix_x+60 and spell.pix_y <= pos[1] <= spell.pix_y+52:
                            if spell.name == "snow":
                                card_num2 = 3
                            elif spell.name == "fire":
                                card_num2 = 4
                            elif spell.name == "lightning":
                                card_num2 = 5


    if card_num2 != int:
        if player_turn == 1:
            card_pic2 = pygame.image.load(card_type[card_num2] + ".png")
        else:
            card_pic2 = pygame.image.load(card_type[card_num2] + "2.png")
        if 0 <= card_num2 <= 2: #Unit
            new_card = cards.Unit(card_num2, card_pic2, c_i_l)
        elif 3 <= card_num2 <= 5: #Spell
            new_card = cards.Spell(card_num2, card_pic2, c_i_l)
        elif 6 <= card_num2 <= 8: #Defense
            new_card = cards.Defense(card_num2, card_pic2, c_i_l)
            
        elif 9 <= card_num2 <= 11: #Production
             new_card = cards.Production(card_num2, card_pic2, c_i_l)

        screen.blit(new_card.image, [621, 575])
        card_cost = font.render(str(new_card.cost), True, white)
        screen.blit(card_cost, [635, 640])
        if isinstance(new_card, cards.Spell) == False:
            card_health = font.render("Health", True, white)
            card_health2 = font.render(str(new_card.health), True, white)
            screen.blit(card_health, [536, 575])
            screen.blit(card_health2, [536+15,575+35])
        if isinstance(new_card, cards.Unit) == True or isinstance(new_card, cards.Defense) == True:
            card_damage = font.render("Dmg", True, white)
            card_damage2 = font.render(str(new_card.damage), True, white)                    
            screen.blit(card_damage, [710, 575])
            screen.blit(card_damage2, [710+10,575+35])
        if isinstance(new_card, cards.Production) == True:
            card_damage = font.render("Spawn", True, white)
            card_damage2 = font.render(new_card.production_type, True, white)                    
            screen.blit(card_damage, [700, 575])
            screen.blit(card_damage2, [700+5,575+35])
