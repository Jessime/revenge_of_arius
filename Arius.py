import pygame, buttons, mails

def start_menu():
    pygame.init() # Initialize the game engine
    screen = pygame.display.set_mode([540, 720])# Set the height and width of the screen
    start, turn = (False,)*2 #Initialize
    mouse = pygame.image.load("tree_cursor.png") #Upload hover mouse image
    background = pygame.image.load("start_menu.png")# Set the screen background
    pygame.time.set_timer(pygame.USEREVENT+1, 5000) #Set timer to check player turn every 5s
    
    while start == False:
        screen.blit(background, [0,0])
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                start = True # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN: #User clicks the mouse.
                pos = pygame.mouse.get_pos() #Get the position
                for btn in buttons.btn_dic.values():
                    btn.check_dclick(pos)
            elif event.type == pygame.MOUSEBUTTONUP:# User clicks the mouse. 
                pos = pygame.mouse.get_pos() #Get the position
                for btn in buttons.btn_dic.values():
                    btn.check_uclick(pos)
            elif event.type == pygame.USEREVENT+1:
                player_turn, p1_name, p2_name = mails.auto_get_mail()
                player = mails.check_file(True)
                #print(player, player_turn, p1_name, p2_name)
                if ((player_turn == player[0] and
                    p1_name == player[1]) or
                    (player_turn == player[0] and
                    p2_name == player[1])):
                    turn = True
                else:
                    turn = False

        buttons.updating(screen, turn) #Update button hover/click/action info
        pygame.display.flip()#Update

    # Clears button dictionary
    buttons.btn_dic.clear()

start_menu()
pygame.quit()
