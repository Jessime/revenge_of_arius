# import all other necessary files
import pygame, time, random, nodes, events, gather, track_card, turn_update, screen_graphics, unit_stats, gamer, textbox

def game(p1_name, p2_name, *args):
    #Initialize everything
    clock = pygame.time.Clock()
    countdown = 45
    grid,card_list,card_pics,popup = [], [], [], [] #All lists
    card_type = ["elf", "santa", "reindeer", "snow", "fire", "lightning", "wood", "brick", "castle", "mine", "factory", "northpole"]
    pick_card = False #Defaults for cards
    card_num, action, rand_x, rand_y = (int,)*4
    player_turn = 1
    card_info_list = unit_stats.unit_stats() # Get card information
    done, start, end_click, bag_visible, button, correct, gather_mana, bag_clicked = (False,)*8 #Flags 
    mana_increase = 110     
    p1 = gamer.Player(2500, 100, 100, 105, p1_name) # Create players 
    p2 = gamer.Player(2500, 100, 100, 105, p2_name)
    text_btn = textbox.init_textbox(918, 10, 100, 60) # Create textbox
    screen = pygame.display.set_mode([1300, 675])
    
    # Create the playing board
    for y in range(8):
        grid.append([])
        for x in range(16):
            grid[y].append(nodes.Node(x,y))
            
    player_turn, p1, p2, mana_increase, card_list, card_pics = turn_update.init_update(player_turn, p1, p2, mana_increase,
                                                                                       grid, card_type, card_pics, card_list, args) #setup initalized variables

    # Initialize Timer    
    start_time = time.time()

    # Main loop
    while not done:
        #Draw all mainscreen objects
        display_timer = screen_graphics.render_main(screen, player_turn, end_click, card_list, p1, p2, countdown, start_time, grid, popup)

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pick_card, card_num, x, y, bag_visible, gather_mana, popup = events.downclick(pick_card, player_turn, card_num, card_list,
                                                                                        p1, p2, card_pics, grid, screen, rand_x, rand_y,
                                                                                        bag_visible, gather_mana, popup)
            elif event.type == pygame.MOUSEBUTTONUP:
                countdown, display_timer , correct = events.upclick(countdown, text_btn, display_timer, gather_mana, mana_increase, correct)
            elif event.type == pygame.KEYDOWN and text_btn.selected:
                input_entered = text_btn.char_add(event)
                
        # Card follows mouse on selection of card
        track_card.tracking(screen, pick_card, card_num, card_type, player_turn, card_list)

        # Mana
        if display_timer == 36:
            rand_x, rand_y, = gather.get_random()
            bag_visible = True
        if 15 < display_timer <= 35:
            gather.gather_mana(rand_x, rand_y, bag_visible, grid, screen)
            gather.gathering(gather_mana, correct, mana_increase, screen, player_turn, text_btn)
            correct, gather_mana = gather.gathered(correct, gather_mana, text_btn, p1, p2, player_turn, mana_increase)
                    
        if display_timer == 25:
            bag_visible, gather_mana = gather.reset_gather(text_btn)

        # Update at the end of a turn
        if display_timer <= 0:
            player_turn, card_list, mana_increase, popup, pick_card, done = turn_update.stats_update(player_turn, p1, p2, card_list, card_pics, grid, mana_increase, popup, pick_card)

        # Update the screen
        pygame.display.flip()
