import os, sys, pygame, produce, unit_stats, cards, damage, random, mails, buttons

def init_update(player_turn, p1, p2, mana_increase, grid, card_type, card_pics, card_list, args):
    player_turn = 1
    buttons.new_game.clicked = False
    pygame.display.set_caption("The Revenge of Arius")
    buttons.btn_dic["end_turn"] = buttons.end_turn #Adds endturn btn to screen
    for card in card_type:
        card_pics.append(pygame.image.load(card + ".png"))
    for card in card_type:
        card_pics.append(pygame.image.load(card + "2.png"))
    
    if args != ():
        player_turn, p1, p2, mana_increase, card_list = args[0], args[1], args[2], args[3], args[4]
        for card in card_list:
            grid[card.y][card.x].occupants_list.append(card)
    for y in range(8):
        for x in range(16):
            grid[y][x].fog_of_war(player_turn, card_list)

    return player_turn, p1, p2, mana_increase, card_list, card_pics

def loc_update(player_turn, p1, p2, card_list, grid):
    # Update unit location for card 1
    if player_turn == 1:
        for card in card_list:
            # Check if unit should move forward
            if (isinstance(card, cards.Unit) == True and 
                card.p_designation == 1 and
                card.x < 14):
                card.move_card1(card_list, grid)
        card_list, p1, p2 = damage.damage_update(card_list, p1, p2, grid)        
    if player_turn == 2:
        for card in card_list:
            # Check if unit should move forward
            if (isinstance(card, cards.Unit) == True and 
                card.p_designation == 2 and
                card.x > 1):
                card.move_card2(card_list, grid)
        card_list, p1, p2 = damage.damage_update(card_list, p1, p2, grid)    

def spell_update(card_list, grid, player_turn):
    for card in card_list:
        if isinstance(card, cards.Spell) and player_turn == card.p_designation:
            card.check_duration()
            if card.duration == 0: #remove card from all lists
                card_list.remove(card) 
                grid[card.y][card.x].occupants_list.remove(card)

def file_update(p1, p2, card_list): #Stores history of health, mana, cards for a game
    if os.path.isfile(os.path.dirname(sys.argv[0])+"\\health.txt"):
        h_file = open("health.txt", "r")
        h_str = h_file.read()
        h_file.close()
        h_list = h_str.split()
        turn = int(h_list[-3])
        new_turn = turn+1
        new_h_file = open("health.txt", "w")
        new_h_file.write(h_str+" "+str(new_turn)+" "+str(p1.health)+" "+str(p2.health))
        new_h_file.close()
    else:
        new_h_file = open("health.txt", "w")
        new_h_file.write(str(1)+" "+str(p1.health)+" "+str(p2.health))
        new_h_file.close()
    if os.path.isfile(os.path.dirname(sys.argv[0])+"\\mana.txt"):
        m_file = open("mana.txt", "r")
        m_str = m_file.read()
        m_file.close()
        m_list = m_str.split()
        turn = int(m_list[-3])
        new_turn = turn+1
        new_m_file = open("mana.txt", "w")
        new_m_file.write(m_str+" "+str(new_turn)+" "+str(p1.mana)+" "+str(p2.mana))
        new_m_file.close()
    else:
        new_m_file = open("mana.txt", "w")
        new_m_file.write(str(1)+" "+str(p1.mana)+" "+str(p2.mana))
        new_m_file.close()

    counter1 = 0
    counter2 = 0
    for card in card_list:
        if card.p_designation == 1:
            counter1 += 1
        else:
            counter2 +=1

    if os.path.isfile(os.path.dirname(sys.argv[0])+"\\cards.txt"):
        c_file = open("cards.txt", "r")
        c_str = c_file.read()
        c_file.close()
        c_list = c_str.split()
        turn = int(c_list[-3])
        new_turn = turn+1
        new_c_file = open("cards.txt", "w")
        new_c_file.write(c_str+" "+str(new_turn)+" "+str(counter1)+" "+str(counter2))
        new_c_file.close()
    else:
        new_c_file = open("cards.txt", "w")
        new_c_file.write(str(1)+" "+str(counter1)+" "+str(counter2))
        new_c_file.close()
        
def stats_update(player_turn, p1, p2, card_list, card_pics, grid, mana_increase, popup, pick_card):
    card_info_list = unit_stats.unit_stats()
    pick_card = False
    done = True
    screen = pygame.display.set_mode([540, 720])
    background = pygame.image.load("start_menu.png")
    screen.blit(background, [0,0])
    pygame.display.flip()#Switch screens before lagging while checking mail

    loc_update(player_turn, p1, p2, card_list, grid)
    spell_update(card_list, grid, player_turn)
    if popup != []:
        grid[popup[1]][popup[0]].close_pop() # Close the popup window if opened
        popup = [] # Reset popup window
    for card in card_list:
        if isinstance(card, cards.Unit):
            card.casting = False

    if player_turn == 1:
        player_turn = 2
        p1, card_list = produce.produce1(card_list, card_info_list, card_pics, grid, p1)
        p1.gold = p1.gold_inc
        p1.gold_inc = int(p1.gold_inc ** 1.012)
        p1.mana += 20
    else:
        player_turn = 1
        p2, card_list = produce.produce2(card_list, card_info_list, card_pics, grid, p2)
        p2.gold = p2.gold_inc
        p2.gold_inc = int(p2.gold_inc ** 1.012)
        mana_increase = int(mana_increase * 1.09) + random.randint(-5, 5)
        p2.mana += 20

    file_update(p1, p2, card_list)
    mails.send_mail(player_turn, mana_increase, p1, p2, card_list)
    return player_turn, card_list, mana_increase, popup, pick_card, done

