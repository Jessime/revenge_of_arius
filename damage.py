import pygame, cards
            
def damage_update(card_list, p1, p2, grid):
    for card in card_list:
        if (card.p_designation == 1 and 
            isinstance(card, cards.Spell) != True and
            len(grid[card.y][card.x + 1].occupants_list) != 0): #Unit/Defense attacks card
            grid[card.y][card.x + 1].damage_sort(card, card_list) 
        # If unit attacks player
        if card.p_designation == 1 and card.x == 14:
            enemy = 0
            for card2 in card_list:
                if card2.x == 15 and card2.y == card.y:
                    enemy += 1
            if enemy == 0:
                p2.health -= card.damage
                
        # If spell attacks card
        if card.p_designation == 1 and isinstance(card, cards.Spell) == True:
            for card3 in card_list:
                if (card3.p_designation == 2 and 
                    card3.x == card.x and
                    card3.y == card.y and 
                    isinstance(card3, cards.Spell) != True):
                    
                    card3.health -= card.damage
                    if card3.health <= 0:
                        grid[card3.y][card3.x].occupants_list.remove(card3)
                        card_list.remove(card3)
        if (card.p_designation == 2 and
            isinstance(card, cards.Spell) != True and
            len(grid[card.y][card.x - 1].occupants_list) != 0):
            grid[card.y][card.x - 1].damage_sort(card, card_list)                
        # If unit attacks player   
        if card.p_designation == 2 and card.x == 1:
            enemy = 0
            for card4 in card_list:
                if card4.x == 0 and card4.y == card.y:
                    enemy += 1
            if enemy == 0:
                p1.health -= card.damage
                
        # If spell attacks card
        if card.p_designation == 2 and isinstance(card, cards.Spell) == True:
            for card5 in card_list:
                if (card5.p_designation == 1 and
                    card5.x == card.x and
                    card5.y == card.y and
                    isinstance(card5, cards.Spell) != True):
                    card5.health -= card.damage
                    if card5.health <= 0:
                        grid[card5.y][card5.x].occupants_list.remove(card5)
                        card_list.remove(card5)
    return card_list, p1, p2
        
def do_spell_damage(card, card2):
    spell = card.name
    if isinstance(card2, cards.Unit) == True:
        if spell == "ice":
            card2.health -= card.damage - card2.ice_resistance
        if spell == "fire":
            card2.health -= card.damage - card2.fire_resistance
        if spell == "lightning":
            card2.health -= card.damage - card2.lightning_resistance
    else:
        card2.health -= card.damage
