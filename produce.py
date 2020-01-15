import random, cards

def produce1(card_list, card_info_list, card_pics, grid, p1):
    for card in card_list:
        if (card.name == "mine" and
            card.p_designation == 1):
            p1.mana += 25
        if (card.name == "factory" and
            card.p_designation == 1 and
            card.pro_rate == 0):
                card.pro_rate = 1
        elif (card.name == "factory" and
              card.p_designation == 1 and
              card.pro_rate == 1):
            #Create brick card
            new_defense = cards.Defense(7, card_pics[7], card_info_list)
            #Produce bricks in a line
            placed = 0
            i = 1
            y_val = 0
            while placed != 1 and i <= 8:
                walled = 0
                if i + card.y <= 7:
                    for card2 in grid[card.y + i][card.x].occupants_list:
                        if card2.name == "brick":
                            walled = 1
        
                elif i + card.y > 7:
                    for card2 in grid[(card.y + i)-8][card.x].occupants_list:
                        if card2.name == "brick":
                            walled = 1
                if walled == 0 and i + card.y <= 7:
                    y_val = card.y + i
                    placed = 1
                elif walled == 0 and i + card.y > 7:
                    y_val = (card.y + i) - 8
                    placed = 1 
                elif walled == 1:
                    pass
                i += 1
            if placed == 0:
                y_val = random.randint(0, 7)
            
    
            new_defense.x, new_defense.y = grid[y_val][card.x].add_card(new_defense)
            new_defense.draw_card()
            card_list.append(new_defense)
            new_defense.p_designation = 1
            #set production_rate back to 0
            card.pro_rate = 0
        if (card.name == "northpole" and
            card.p_designation == 1):
                #Create elf
                new_unit = cards.Unit(0, card_pics[0], card_info_list)
                new_unit.x, new_unit.y = grid[card.y][0].add_card(new_unit)
                new_unit.draw_card()
                card_list.append(new_unit)
                new_unit.p_designation = 1

    return p1, card_list

def produce2(card_list, card_info_list, card_pics, grid, p2):
    for card in card_list:
        if (card.name == "mine" and
            card.p_designation == 2):
            p2.mana += 25
        if (card.name == "factory" and
            card.p_designation == 2 and
            card.pro_rate == 0):
                card.pro_rate = 1
        elif (card.name == "factory" and
              card.p_designation == 2 and
              card.pro_rate == 1):
            #Create brick card
            new_defense = cards.Defense(7, card_pics[19], card_info_list)
            #Produce bricks in a line
            placed = 0
            i = 1
            y_val = 0
            while placed != 1 and i <= 8:
                walled = 0
                if i + card.y <= 7:
                    for card2 in grid[card.y + i][card.x].occupants_list:
                        if card2.name == "brick":
                            walled = 1
        
                elif i + card.y > 7:
                    for card2 in grid[(card.y + i)-8][card.x].occupants_list:
                        if card2.name == "brick":
                            walled = 1
                if walled == 0 and i + card.y <= 7:
                    y_val = card.y + i
                    placed = 1
                elif walled == 0 and i + card.y > 7:
                    y_val = (card.y + i) - 8
                    placed = 1 
                elif walled == 1:
                    pass
                i += 1
            if placed == 0:
                y_val = random.randint(0, 7)
            
    
            new_defense.x, new_defense.y = grid[y_val][card.x].add_card(new_defense)
            new_defense.draw_card()
            card_list.append(new_defense)
            new_defense.p_designation = 2
            #set production_rate back to 0
            card.pro_rate = 0
        if (card.name == "northpole" and
            card.p_designation == 2):
                #Create elf
                new_unit = cards.Unit(0, card_pics[12], card_info_list)
                new_unit.x, new_unit.y = grid[card.y][15].add_card(new_unit)
                new_unit.draw_card()
                card_list.append(new_unit)
                new_unit.p_designation = 2

    return p2, card_list
