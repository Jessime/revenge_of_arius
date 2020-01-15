import pygame, timer, cards, buttons
black = [  0,   0,   0]
white = [255, 255, 255]
main_castle = pygame.image.load("castle9.png")
main_castle2 = pygame.image.load("castle8.png")
card_pics2 = ["elf", "santa", "reindeer", "wood", "brick", "castle", "mine", "factory", "northpole"]
end1 = pygame.image.load("end_turn1-2.png")
end2 = pygame.image.load("end_turn2-2.png")
info_card = pygame.image.load("info_card.png")
info_card2 = pygame.image.load("info_card2.png")
info_card3 = pygame.image.load("info_card3.png")
info_card6 = pygame.image.load("info_card6.png")
       
def draw_static(screen):
    screen.blit(main_castle, [0,0])
    screen.blit(main_castle2, [1150,0])
    pygame.draw.rect(screen, black, [150, 120, 999, 435], 4)
    for y_offset in range(0, 450, 54):
        pygame.draw.line(screen, black, [153, 120 + y_offset], [1145, 120+ y_offset], 2)
    for x_offset in range(0, 1000, 62):
        pygame.draw.line(screen, black, [153+ x_offset, 120], [153+ x_offset, 552], 2)
    for i in range(0, 245, 82): # Draw background cards
        screen.blit(info_card, [150+i, 557])
        screen.blit(info_card2, [905+i, 557])
        screen.blit(info_card3, [528+i, 557])
    
def draw_cards(screen, player_turn):
    width2 = 62
    for element in card_pics2:
        if player_turn == 1:
            picture = pygame.image.load(element + ".png")
            screen.blit(picture, [250 + width2, 33])    
            width2 += 62
        if player_turn == 2:
            picture = pygame.image.load(element + "2.png")
            screen.blit(picture, [250 + width2, 33])    
            width2 += 62
    
# Draw Spells in popup window
def draw_spells(card, screen):
    if card.spell_list != []:
        for spell in card.spell_list:
            screen.blit(spell.image, [spell.pix_x, spell.pix_y])

            
# Draw player turn
def draw_turn(screen, player_turn, p1, p2):
    font = pygame.font.Font(None, 30)
    screen.blit(info_card3, [396, 557])
    turn = font.render("Turn",True,white)
    screen.blit(turn, [410, 575])   
    if player_turn == 1:
        p_turn = font.render(p1.name ,True,white)
    if player_turn == 2:
        p_turn = font.render(p2.name ,True,white)
    screen.blit(p_turn, [410-5, 575+35])

# Draw card stats on hover inside popup
def draw_card_info(screen, popup, grid):
    font = pygame.font.Font(None, 30)
    pos = pygame.mouse.get_pos()

    for pop_card in grid[popup[1]][popup[0]].occupants_list:
        
        if pop_card.pix_y != grid[popup[1]][popup[0]].pix_y and pop_card.pix_x <= pos[0] <= pop_card.pix_x + 60 and pop_card.pix_y <= pos[1] <= pop_card.pix_y + 52: #If card is hovered
            screen.blit(pop_card.image, [621, 575])
            if isinstance(pop_card, cards.Spell) == False:
                card_health = font.render("Health", True, white)
                card_health2 = font.render(str(pop_card.health), True, white)
                screen.blit(card_health, [536, 575])
                screen.blit(card_health2, [536+15,575+35])
            if isinstance(pop_card, cards.Production) == False:
                card_damage = font.render("Dmg", True, white)
                card_damage2 = font.render(str(pop_card.damage), True, white)                    
                screen.blit(card_damage, [710, 575])
                screen.blit(card_damage2, [710+10,575+35])
            if isinstance(pop_card, cards.Spell) == True:
                card_duration = font.render("Span", True, white)
                card_duration2 = font.render(str(pop_card.duration), True, white)
                screen.blit(card_duration, [544, 575])
                screen.blit(card_duration2, [544+15,575+35])
            if isinstance(pop_card, cards.Production) == True:
                card_pro_rate = font.render("Next", True, white)
                card_pro_rate2 = font.render(str(pop_card.pro_rate), True, white)
                screen.blit(card_pro_rate, [710, 575])
                screen.blit(card_pro_rate2, [710+15,575+35])            
            

def render_main(screen, player_turn, end_click, card_list, p1, p2, countdown, start_time, grid, popup):
    screen.fill(white) # Set the screen background
    # Draw player turn, card grid, nodes, end
    draw_turn(screen, player_turn, p1, p2)
    draw_static(screen)
    p1.draw_stats(screen, [158, 575], [249, 575], [327, 575], black)
    p2.draw_stats(screen, [913, 575], [1003, 575], [1083, 575], black)
    screen.blit(info_card6, [290, 7])
    draw_cards(screen, player_turn)

    # Render all clickable buttons
    for btn in buttons.btn_dic.values():
        screen.blit(btn.visible, [btn.x1, btn.y1])
        btn.check_hover(buttons.btn_dic)
        btn.update(screen)

    # Draw all cards on the grid
    for card in card_list:
        screen.blit(card.image, [card.pix_x, card.pix_y])

    #Draw fog
    for i in range(8):
        for j in range(16):
            grid[i][j].show_fog(screen)    

    # Create popup window to see cards in the node and cast spells
    if popup != []:
        draw_card_info(screen, popup, grid)
        grid[popup[1]][popup[0]].pop_up(screen)
        
    for card2 in card_list: #card2 necessary because of blit order for popup
        
        if isinstance(card2, cards.Unit):
            draw_spells(card2, screen)
            if card2.casting == True:
                card2.add_spell(grid, screen)
            
    # Create the timer
    screen.blit(info_card3, [823, 557])
    display_timer = timer.timer(countdown, start_time, screen)
               
    return display_timer
