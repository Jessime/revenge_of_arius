import pygame, textbox, play_cards, cards, gather, buttons

def downclick(pick_card, player_turn, card_num, card_list,
              p1, p2, card_pics, grid, screen, rand_x, rand_y,
              bag_visible, gather_mana, popup):
    # Set the width, height, margin of each grid location
    width  = 60
    height = 52
    margin = 2

    spell_visible = False
    # Initialize grid coordinates
    x = int
    y = int
    # User clicks the mouse. Get the position
    pos = pygame.mouse.get_pos()
    if (153 < pos[0] < 1145) and (120 < pos[1] < 552):
        
        # Change the x/y screen coordinates to grid coordinates if popup window isn't open
        if popup == []:
            x = (pos[0]-153) // (width + margin)
            y = (pos[1]-120) // (height + margin)
            # Check if mana bag has been clicked
            if bag_visible == True and rand_x == x and rand_y == y:
                bag_visible = False
                gather_mana = True
                buttons.btn_dic["gather_btn"] = buttons.gather_btn  
            # Check if card has been selected
            elif pick_card == True:
                pick_card = False
                action = play_cards.placement_check(player_turn, card_num, p1, p2, x, y, popup, card_list)
                play_cards.place_card(action, card_num, card_pics, card_list, grid, x, y, p1, p2, player_turn)
            # Check if pop_up window should be created or closed
            elif (len(grid[y][x].occupants_list) != 0 and
                  grid[y][x].fogged == False):
                popup = [x, y]          

        elif popup != []: #If popup is open
            # Check if spells should be displayed for casting in pop_up window
            for pop_card in grid[popup[1]][popup[0]].occupants_list:
                if (pop_card.pix_x <= pos[0] <= pop_card.pix_x + 60 and
                    pop_card.pix_y <= pos[1] <= pop_card.pix_y + 52 and
                    pop_card.p_designation == player_turn and
                    isinstance(pop_card, cards.Unit)): #If unit is clicked
                    if pop_card.spell_list == []: #If spells aren't showing
                        pop_card.pop_spells(card_pics) #Show spells
                        spell_visible = True
                elif isinstance(pop_card, cards.Unit): 
                    for spell_card in pop_card.spell_list:
                        if spell_card.pix_x <= pos[0] <= spell_card.pix_x + 60 and spell_card.pix_y <= pos[1] <= spell_card.pix_y + 52:
                            pop_card.casting = True #Signals a Unit attempting to casting a spell
                            pick_card = True
                            if popup[1] <= 3: # For the top half
                                card_num = ((pos[1]-(pop_card.pix_y + 52))// (height+margin))+ 3 # Weird math to find card number based on pixel location
                            else: # For the bottom half
                                card_num = ((pop_card.pix_y - (pos[1]-2))// (height+margin))+ 3
      

            # Close the pop up window
            if spell_visible == False: 
                grid[popup[1]][popup[0]].close_pop()
                popup = []
      

    # Check if card is clicked
    elif (312 <= pos[0] < 498) and (33 < pos[1] < 85):
        card_num = (pos[0]-312)// (width+margin)
        pick_card = True
    elif (498 <= pos[0] < 868) and (33 < pos[1] < 85):
        card_num = (186+(pos[0]-312))// (width+margin)
        pick_card = True
            
    # Check if end turn is clicked
    else:
        for btn in buttons.btn_dic.values():
            btn.check_dclick(pos)
    
    return pick_card, card_num, x, y, bag_visible, gather_mana, popup
                  
def upclick(countdown, text_btn, display_timer, gather_mana, mana_increase, correct):
    pos = pygame.mouse.get_pos()
    """get_mana(button, textbox)"""
    # Check if button is released
    for btn in buttons.btn_dic.values():
        btn.check_uclick(pos)
            
    # Process actions for button clicks
    if buttons.btn_dic["end_turn"].clicked == True:
        buttons.btn_dic["end_turn"].clicked = False
        countdown, display_timer = 0,0
    elif buttons.btn_dic.get("gather_btn") != None:
        if buttons.btn_dic["gather_btn"].clicked == True:
            buttons.btn_dic["gather_btn"].clicked = False
            if text_btn.string == str(mana_increase) and gather_mana == True:
                correct = True
            else:
                text_btn.str_list = [""]
                text_btn.selected = False
            
    # Check if textbox button has been clicked
    if gather_mana == True and text_btn.rect.collidepoint(pos):
        if text_btn.selected == False:
            text_btn.selected = True
        else:
            text_btn.selected = False

    return countdown, display_timer, correct


    

