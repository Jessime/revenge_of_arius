import pygame, time, random, unit_stats, cards

def placement_check(player_turn, card_num, p1, p2, x, y, popup, card_list):
    # Get card information
    card_info_list = unit_stats.unit_stats()
    p1_gold = p1.gold
    p1_mana = p1.mana
    p2_gold = p2.gold
    p2_mana = p2.mana
    action = 0
    if player_turn == 1:
        if 3 <= card_num <= 5:
            for card in card_list:
                if isinstance(card, cards.Unit): #Needed before checking casting
                    if card.casting == True and card.name == "santa":
                        card.casting = False
                        if (card_info_list[card_num][4] <= p1_gold and
                            ((card.x-1 <= x <= card.x+1 and card.y-1 == y) or
                            (card.x-1 <= x <= card.x+1 and card.y+1 == y) or
                            (card.x+1 == x and card.y == y))):
                            action = 2.1 #Spell
                    elif card.casting == True and card.name == "reindeer":
                        card.casting = False
                        if (card_info_list[card_num][4] <= p1_gold and
                            ((card.x+2 == x and card.y-2 == y) or
                            (card.x+2 == x and card.y+2 == y) or
                            (card.x+1 == x and card.y == y))):
                            action = 2.2 #Spell
                    elif card.casting == True and card.name == "elf":
                        card.casting = False
                        if (card_info_list[card_num][4] <= p1_gold and
                            ((card.x == x and card.y-1 >= y >= card.y-2) or
                            (card.x == x and card.y+1 <= y <= card.y+2) or
                            (card.x+1 == x and card.y == y))):
                            action = 2.3 #Spell

        elif x == 0:
            if 0 <= card_num <= 2 and card_info_list[card_num][6] <= p1_gold:
                action = 1 #Unit
        elif 1 <= x <= 3:
            if 6 <= card_num <= 8 and card_info_list[card_num][2] <= p1_mana:
                action = 3 #Defense
            elif 9 <= card_num <= 11 and card_info_list[card_num][3] <= p1_mana:
                action = 4 #Production
                
    else: #Player2
        if 3 <= card_num <= 5:
            for card in card_list:
                if isinstance(card, cards.Unit): #Needed before checking casting
                    if card.casting == True and card.name == "santa":
                        card.casting = False
                        if (card_info_list[card_num][4] <= p2_gold and
                            ((card.x-1 <= x <= card.x+1 and card.y-1 == y) or
                            (card.x-1 <= x <= card.x+1 and card.y+1 == y) or
                            (card.x-1 == x and card.y == y))):
                            action = 6.1 #Spell
                    elif card.casting == True and card.name == "reindeer":
                        card.casting = False
                        if (card_info_list[card_num][4] <= p2_gold and
                            ((card.x-2 == x and card.y-2 == y) or
                            (card.x-2 == x and card.y+2 == y) or
                            (card.x-1 == x and card.y == y))):
                            action = 6.2 #Spell
                    elif card.casting == True and card.name == "elf":
                        card.casting = False
                        if (card_info_list[card_num][4] <= p2_gold and
                            ((card.x == x and card.y-1 >= y >= card.y-2) or
                            (card.x == x and card.y+1 <= y <= card.y+2) or
                            (card.x-1 == x and card.y == y))):
                            action = 6.3 #Spell

        elif x == 15:
            if 0 <= card_num <= 2 and card_info_list[card_num][6] <= p2_gold:
                action = 5 #Unit
        elif 12 <= x <= 14:
            if 6 <= card_num <= 8 and card_info_list[card_num][2] <= p2_mana:
                action = 7
            elif 9 <= card_num <= 11 and card_info_list[card_num][3] <= p2_mana:
                action = 8
    return action

def place_card(action, card_num, card_pics, card_list, grid, x, y, p1, p2, player_turn):
    # Get card information
    card_info_list = unit_stats.unit_stats()
    if action == 1:    
        # If unit is placed
        new_unit = cards.Unit(card_num, card_pics[card_num], card_info_list)
        new_unit.x, new_unit.y = grid[y][x].add_card(new_unit)
        new_unit.draw_card()
        card_list.append(new_unit)
        new_unit.p_designation = 1
        p1.gold -= new_unit.cost
    elif action == 5:
        new_unit = cards.Unit(card_num, card_pics[card_num + 12], card_info_list)
        new_unit.x, new_unit.y = grid[y][x].add_card(new_unit)
        new_unit.draw_card()
        card_list.append(new_unit)
        new_unit.p_designation = 2
        p2.gold -= new_unit.cost

    elif action == 2.1 or action == 2.2 or action == 2.3:    
        # If spell is placed
        new_spell = cards.Spell(card_num, card_pics[card_num], card_info_list)
        new_spell.x, new_spell.y = grid[y][x].add_card(new_spell)
        new_spell.draw_card()
        new_spell.casting_damage(action)
        card_list.append(new_spell)
        new_spell.p_designation = 1
        p1.gold -= new_spell.cost
    elif action == 6.1 or action == 6.2 or action == 6.3:
        new_spell = cards.Spell(card_num, card_pics[card_num + 12], card_info_list)
        new_spell.x, new_spell.y = grid[y][x].add_card(new_spell)
        new_spell.draw_card()
        new_spell.casting_damage(action)
        card_list.append(new_spell)
        new_spell.p_designation = 1
        p1.gold -= new_spell.cost                        
        new_spell.p_designation = 2
        p2.gold -= new_spell.cost
            
    elif action == 3:     
        # If defense is placed
        new_defense = cards.Defense(card_num, card_pics[card_num], card_info_list)
        new_defense.x, new_defense.y = grid[y][x].add_card(new_defense)
        new_defense.draw_card()
        card_list.append(new_defense)
        new_defense.p_designation = 1
        p1.mana -= new_defense.cost
    elif action == 7:
        new_defense = cards.Defense(card_num, card_pics[card_num + 12], card_info_list)
        new_defense.x, new_defense.y = grid[y][x].add_card(new_defense)
        new_defense.draw_card()
        card_list.append(new_defense)
        new_defense.p_designation = 2
        p2.mana -= new_defense.cost

    elif action == 4:   
        # If production is placed is placed
        new_production = cards.Production(card_num, card_pics[card_num], card_info_list)
        new_production.x, new_production.y = grid[y][x].add_card(new_production)
        new_production.draw_card()
        card_list.append(new_production)
        new_production.p_designation = 1
        p1.mana -= new_production.cost
    elif action == 8:
        new_production = cards.Production(card_num, card_pics[card_num + 12], card_info_list)
        new_production.x, new_production.y = grid[y][x].add_card(new_production)
        new_production.draw_card()
        card_list.append(new_production)
        new_production.p_designation = 2
        p2.mana -= new_production.cost 
