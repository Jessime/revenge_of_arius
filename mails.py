import os.path, sys, pygame, smtplib, imaplib, gamer, cards, unit_stats, textbox

def get_name(screen, btn_dic, *two):
    if two:
        info_card = pygame.image.load("info_card8.png")
    else:
        info_card = pygame.image.load("info_card7.png")
        
    loc = [150, 7]
    text_btn = textbox.init_textbox(160, 17, 100, 60)
    done = False
    font = pygame.font.Font(None, 30)
    name = font.render("Name?",True,[0,0,0])
    background = pygame.image.load("start_menu.png")
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btn_dic.values():
                    btn.check_dclick(pos)                
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for btn in btn_dic.values():
                    btn.check_uclick(pos)
                if text_btn.selected == False and text_btn.rect.collidepoint(pos):
                    text_btn.selected = True
                elif text_btn.selected and text_btn.rect.collidepoint(pos):
                    text_btn.selected = False
                elif btn_dic["gather_btn2"].clicked:
                    p_name = text_btn.string
                    del btn_dic["gather_btn2"]
                    done = True
                else:
                    pass

            elif event.type == pygame.KEYDOWN and text_btn.selected:
                input_entered = text_btn.char_add(event)
                
        screen.blit(background, [0,0])
        screen.blit(info_card, loc)
        screen.blit(name, [loc[0]+25, loc[1]+80])
        text_btn.update(screen)
        for btn in btn_dic.values():
            screen.blit(btn.visible, [btn.x1, btn.y1])
            btn.check_hover(btn_dic)
            btn.update(screen)
        pygame.display.flip()
    return p_name
                                      
        
def save_1(p1_name):
    player = open("player.txt", "w")
    player.write("1 " + p1_name)
    player.close()
    
def save_2(p2_name):
    player = open("player.txt", "w")
    player.write("2 " + p2_name)
    player.close()    

def check_file(*auto):
    if os.path.isfile(os.path.dirname(sys.argv[0])+"\\player.txt"):
        p_file = open("player.txt", "r")
        file_str = p_file.read()
        player = file_str.split()
        player[0] = int(player[0])
        p_file.close()
    elif auto:
        player = [None, None]
    else:
        player = [2, None]
        p_file = open("player.txt", "w")
        p_file.write(str(player[0])+" "+str(player[1]))
        p_file.close()
    return player
        

def get_cards(mail_list):
    c_i_l = unit_stats.unit_stats()
    card_list, card_pics = [], []
    card_type = ["elf", "santa", "reindeer", "snow", "fire", "lightning", "wood", "brick", "castle", "mine", "factory", "northpole"]
    for card in card_type:
        card_pics.append(pygame.image.load(card + ".png"))
    for card in card_type:
        card_pics.append(pygame.image.load(card + "2.png"))
    c_mail = mail_list[11:]
    for i,j in enumerate(c_mail):
        new_unit, new_spell, new_defense, new_production = object, object, object, object
        if j == "elf":
            if int(c_mail[i+1]) == 1:
                new_unit = cards.Unit(0, card_pics[0], c_i_l)
                new_unit.p_designation = 1
            else:
                new_unit = cards.Unit(0, card_pics[0+12], c_i_l)
                new_unit.p_designation = 2
        elif j == "santa":
            if int(c_mail[i+1]) == 1:
                new_unit = cards.Unit(1, card_pics[1], c_i_l)
                new_unit.p_designation = 1
            else:
                new_unit = cards.Unit(1, card_pics[1+12], c_i_l)
                new_unit.p_designation = 2   
        elif j == "reindeer":
            if int(c_mail[i+1]) == 1:
                new_unit = cards.Unit(2, card_pics[2], c_i_l)
                new_unit.p_designation = 1
            else:
                new_unit = cards.Unit(2, card_pics[2+12], c_i_l)
                new_unit.p_designation = 2
        if new_unit != object:
            new_unit.x, new_unit.y = int(c_mail[i+2]), int(c_mail[i+3])
            new_unit.health = int(c_mail[i+4])
            new_unit.draw_card()
            card_list.append(new_unit)

        if j == "snow":
            if int(c_mail[i+1]) == 1:
                new_spell = cards.Spell(3, card_pics[3], c_i_l)
                new_spell.p_designation = 1
            else:
                new_spell = cards.Spell(3, card_pics[3+12], c_i_l)
                new_spell.p_designation = 2
        elif j == "fire":
            if int(c_mail[i+1]) == 1:
                new_spell = cards.Spell(4, card_pics[4], c_i_l)
                new_spell.p_designation = 1
            else:
                new_spell = cards.Spell(4, card_pics[4+12], c_i_l)
                new_spell.p_designation = 2
        elif j == "lightning":
            if int(c_mail[i+1]) == 1:
                new_spell = cards.Spell(5, card_pics[5], c_i_l)
                new_spell.p_designation = 1
            else:
                new_spell = cards.Spell(5, card_pics[5+12], c_i_l)
                new_spell.p_designation = 2
        if new_spell != object:
            new_spell.x, new_spell.y = int(c_mail[i+2]), int(c_mail[i+3])
            new_spell.duration = int(c_mail[i+4])
            new_spell.damage = int(c_mail[i+5])
            new_spell.draw_card()
            card_list.append(new_spell)

        if j == "wood":
            if int(c_mail[i+1]) == 1:
                new_defense = cards.Defense(6, card_pics[6], c_i_l)
                new_defense.p_designation = 1
            else:
                new_defense = cards.Defense(6, card_pics[6+12], c_i_l)
                new_defense.p_designation = 2
        elif j == "fence":
            if int(c_mail[i+1]) == 1:
                new_defense = cards.Defense(7, card_pics[7], c_i_l)
                new_defense.p_designation = 1
            else:
                new_defense = cards.Defense(7, card_pics[7+12], c_i_l)
                new_defense.p_designation = 2
        elif j == "castle":
            if int(c_mail[i+1]) == 1:
                new_defense = cards.Defense(8, card_pics[8], c_i_l)
                new_defense.p_designation = 1
            else:
                new_defense = cards.Defense(8, card_pics[8+12], c_i_l)
                new_defense.p_designation = 2
        if new_defense != object:
            new_defense.x, new_defense.y = int(c_mail[i+2]),int(c_mail[i+3])
            new_defense.health = int(c_mail[i+4])
            new_defense.draw_card()
            card_list.append(new_defense)

        if j == "mine":
            if int(c_mail[i+1]) == 1:
                new_production = cards.Production(9, card_pics[9], c_i_l)
                new_production.p_designation = 1
            else:
                new_production = cards.Production(9, card_pics[9+12], c_i_l)
                new_production.p_designation = 2
        elif j == "factory":
            if int(c_mail[i+1]) == 1:
                new_production = cards.Production(10, card_pics[10], c_i_l)
                new_production.p_designation = 1
            else:
                new_production = cards.Production(10, card_pics[10+12], c_i_l)
                new_production.p_designation = 2
        elif j == "northpole":
            if int(c_mail[i+1]) == 1:
                new_production = cards.Production(11, card_pics[11], c_i_l)
                new_production.p_designation = 1
            else:
                new_production = cards.Production(11, card_pics[11+12], c_i_l)
                new_production.p_designation = 2
        if new_production != object:
            new_production.x, new_production.y = int(c_mail[i+2]), int(c_mail[i+3])
            new_production.health = int(c_mail[i+4])
            new_production.pro_rate = int(c_mail[i+5])
            new_production.draw_card()
            card_list.append(new_production)
    return card_list

def send_cards(body, card_list):
    for card in card_list:
        body += (str(card.name)+" "+str(card.p_designation)+" "+
                str(card.x)+" "+str(card.y)+" ")
        if isinstance(card, cards.Spell) == False:
            body += " "+str(card.health)+" "
        else:
            body += " "+str(card.duration)+" "+str(card.damage)+" "
        if isinstance(card, cards.Production) == True:
            body += " "+str(card.pro_rate)+" "
    return body
    
def auto_get_mail():
    message_server = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    user_name = "arius.revenge@gmail.com"
    password = "computergame123"
    message_server.login(user_name, password)
    stat,count = message_server.select('Inbox')
    stat,content = message_server.fetch(count[0], '(UID BODY[TEXT])')
    mail = str(content[0][1])
    message_server.close()
    message_server.logout()
    player_turn = int(mail[2])
    mail = mail[4:]
    mail_list = mail.split()
    p1_name, p2_name = mail_list[5], mail_list[10]
    return player_turn, p1_name, p2_name
    
def get_mail():
    message_server = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    user_name = "arius.revenge@gmail.com"
    password = "computergame123"
    message_server.login(user_name, password)
    stat,count = message_server.select('Inbox')
    stat,content = message_server.fetch(count[0], '(UID BODY[TEXT])')
    mail = str(content[0][1])
    message_server.close()
    message_server.logout()
    player_turn = int(mail[2])
    mail = mail[4:]
    mail_list = mail.split()
    mana_increase = int(mail_list[0])
    p1 = gamer.Player(int(mail_list[1]), int(mail_list[2]), int(mail_list[3]), int(mail_list[4]), mail_list[5])
    p2 = gamer.Player(int(mail_list[6]), int(mail_list[7]), int(mail_list[8]), int(mail_list[9]), mail_list[10]) 
    card_list = get_cards(mail_list)
    return player_turn, p1, p2, mana_increase, card_list

def send_mail(player_turn, mana_increase, p1, p2, card_list):
    subject = "Python email"
    body = (str(player_turn)+" "+
            str(mana_increase)+" "+
            str(p1.health)+" "+str(p1.gold)+" "+str(p1.mana)+" "+str(p1.gold_inc)+" "+ str(p1.name)+" "+
            str(p2.health)+" "+str(p2.gold)+" "+str(p2.mana)+" "+str(p2.gold_inc)+" "+ str(p2.name)+" ")
    body = send_cards(body, card_list)        
    content = 'Subject: %s\n\n%s' % (subject, body)
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login("arius.revenge@gmail.com", "computergame123")
    mail.sendmail("arius.revenge@gmail.com", "arius.revenge@gmail.com", content)
    mail.close()
