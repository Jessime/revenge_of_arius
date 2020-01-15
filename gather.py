import pygame, random, textbox, buttons

def get_random():
    rand_column = random.randint(1, 14)
    rand_row = random.randint(0, 7)
    return rand_column, rand_row     

# Draw the mana bag during allowed time as long as the bag hasn't been clicked    
def gather_mana(rand_x, rand_y, bag_visible, grid, screen):
    if bag_visible == True:
        bag = pygame.image.load("present_bag.png")
        screen.blit(bag, [grid[rand_y][rand_x].pix_x, grid[rand_y][rand_x].pix_y])
        
# Draw textbox and mana button during allowed time if the mana bag has been clicked
def gathering(gather_mana, correct, mana_increase, screen, player_turn, text_btn):
    font = pygame.font.Font(None, 30)
    info_card7 = pygame.image.load("info_card7.png")
    info_card8 = pygame.image.load("info_card8.png")
    if gather_mana == True and correct == False:
        num_text1 = font.render("Mana ",True,[0,0,0])
        num_text2 = font.render(str(mana_increase),True,[0,0,0])
        if player_turn == 1:
            screen.blit(info_card7, [906, 0])
        else:
            screen.blit(info_card8, [906, 0])
        screen.blit(num_text1, [940, 72])
        screen.blit(num_text2, [945, 92])
        text_btn.update(screen)

# Called if mana has been correctly entered. Gives player mana.
def gathered(correct, gather_mana, text_btn, p1, p2, player_turn, mana_increase):
    if correct == True:
        correct = False
        gather_mana = False
        text_btn.selected = False
        text_btn.str_list = [""]
        text_btn.string= ''.join(text_btn.str_list)
        del buttons.btn_dic["gather_btn"]
        # If player1 gained mana
        if player_turn == 1:
            p1.mana += mana_increase
        # If player2 gained mana
        elif player_turn == 2:
            p2.mana += mana_increase
    return correct, gather_mana

def reset_gather(text_btn):
    bag_visible = False
    gather_mana = False
    text_btn.selected = False
    text_btn.str_list = [""] 
    text_btn.string = ''.join(text_btn.str_list)
    # Delete the gather button from list if it hasn't been already
    if buttons.btn_dic.get("gather_btn") != None:
        del buttons.btn_dic["gather_btn"]
    return bag_visible, gather_mana

        
        
        
