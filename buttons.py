
import pygame, Christmas_Main4, mails, end, audio

#Upload hover mouse image
mouse = pygame.image.load("tree_cursor.png")

class Button ():
    def __init__(self, pic1, pic2, corner):
        self.pic1 = pic1
        self.pic2 = pic2
        self.visible = pic1
        self.x1 = corner[0]
        self.y1 = corner[1]
        self.x2 = pygame.Surface.get_width(pic1) + corner[0]
        self.y2 = pygame.Surface.get_height(pic1) + corner[1]
        self.hover = False
        self.clicked = False

    def check_hover(self, btn_dic):
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        hover_counter = 0
        for btn in btn_dic.values():
            if btn.x1 < x < btn.x2 and btn.y1 < y < btn.y2:
                hover_counter += 1
                pygame.mouse.set_visible(False)
                self.hover = True
        if hover_counter == 0:
            self.hover = False
            pygame.mouse.set_visible(True)
    def check_dclick(self, pos):
        x = pos[0]
        y = pos[1]
        if self.x1 < x < self.x2 and self.y1 < y < self.y2:
            self.visible = self.pic2
        else:
            self.visible = self.pic1
    def check_uclick(self, pos):
        x = pos[0]
        y = pos[1]
        if self.x1 < x < self.x2 and self.y1 < y < self.y2:
            self.visible = self.pic1
            self.clicked = True
    def update(self, screen):
        pos = pygame.mouse.get_pos()     
        if self.hover == True:
            screen.blit(mouse, pos)

button_names = ["new_game", "take_turn", "game_info", "options_menu", "next", "back", "gather", "end_turn"]

btn_pics = []
for btn in button_names:
    btn_pics.append(pygame.image.load(btn + "1.png"))
for btn in button_names:
    btn_pics.append(pygame.image.load(btn + "2.png"))

new_game = Button(btn_pics[0], btn_pics[8], [10, 10])
take_turn = Button(btn_pics[1], btn_pics[9], [10, 115])
game_info = Button(btn_pics[2], btn_pics[10], [10, 220])
options_menu = Button(btn_pics[3], btn_pics[11], [10, 325])
next_btn = Button(btn_pics[4], btn_pics[12], [0, 0])
back_btn = Button(btn_pics[5], btn_pics[13], [0, 0])
gather_btn = Button(btn_pics[6], btn_pics[14], [1030, 7])
end_turn = Button(btn_pics[7], btn_pics[15], [150, 7])
gather_btn2 = Button(btn_pics[6], btn_pics[14], [274, 7])


btn_dic = {"new_game": new_game, "take_turn": take_turn, "game_info": game_info, "options_menu": options_menu}


def updating(screen, turn):
    red = (255,0,0)
    for btn in btn_dic.values():
        screen.blit(btn.visible, [btn.x1, btn.y1])
        btn.check_hover(btn_dic)
        btn.update(screen)
        if turn:
            pygame.draw.rect(screen, red, [10, 115, 123, 94], 3)
    btn_actions(screen)

def btn_actions(screen):
    global btn_dic
    if new_game.clicked:
        btn_dic.update({"gather_btn2": gather_btn2}) #Add btn to get name
        p1_name = mails.get_name(screen, btn_dic) #Let player2 choose name
        btn_dic = {} #Clear the dictionary
        mails.save_1(p1_name) #Save player1 with new name
        Christmas_Main4.game(p1_name, None) #Start the game turn
        screen = pygame.display.set_mode([540, 720])#Reset
        del btn_dic["end_turn"] 
        btn_dic = {"new_game": new_game, "take_turn": take_turn, "game_info": game_info, "options_menu": options_menu}
        
    elif take_turn.clicked:
        take_turn.clicked = False
        player_turn, p1, p2, mana_increase, card_list = mails.get_mail() #Get game state info
        player = mails.check_file() #See if player exists yet
        if player[1] == None: #If player doesn't exist
            btn_dic.update({"gather_btn2": gather_btn2})#Add btn to get name
            p2_name = mails.get_name(screen, btn_dic, True) #Let player2 choose name
            mails.save_2(p2_name)
            p2.name = p2_name #Set player2's name
        if p1.health <= 0 or p2.health <= 0: #Check to see if game is over
            end.end_game(p1, p2)
        elif player_turn == player[0]: #If it's player's turn
            btn_dic = {} #Clear the dictionary
            Christmas_Main4.game(p1.name, p2.name, player_turn, p1, p2, mana_increase, card_list) #Start the game turn
            screen = pygame.display.set_mode([540, 720])#Reset
            del btn_dic["end_turn"]
            btn_dic = {"new_game": new_game, "take_turn": take_turn, "game_info": game_info, "options_menu": options_menu}
        else:
            pass

    elif game_info.clicked:
        game_info.clicked = False
        audio.tutorial()
