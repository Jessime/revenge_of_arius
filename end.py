import pygame, os, sys

class Graph:
    def __init__(self, location, x_max, y_max, x_label, y_label, file, screen):
        self.black = [0, 0, 0]
        self.orange = [255, 140, 0]
        self.purple =  [150,0,150]
        self.screen = screen
        self.loc = location
        self.x1 = location[0] 
        self.y1 = location[1] 
        self.x2 = location[0] + location[2]
        self.y2 = location[1] + location[3]
        self.pad = 35
        self.font = pygame.font.SysFont('Arial', 30)
        self.border = pygame.draw.rect(self.screen, self.black, self.loc, 4)
        self.x_max = x_max
        self.y_max = y_max
        self.x_label = x_label
        self.y_label = y_label
        self.file = open(file,"r")
        self.data = []
        self.pts1 = []
        self.pts2 = []

        

    def get_data(self):
        data_str = self.file.read()
        self.data = data_str.split()
        for i in range(0, len(self.data), 3):
            self.pts1.append([self.data[i], self.data[i+1]])
            self.pts2.append([self.data[i], self.data[i+2]])
        #print(self.pts1)
        #print(self.pts2)

    def convert(self):
        x_unit = (self.x2-self.x1-(self.pad*2))/self.x_max
        y_unit = (self.y2-self.y1-(self.pad*2))/self.y_max
        for pt in self.pts1:
            if int(pt[1]) < 0:
                pt[1] = 0
            pt[0] = int(self.x1 + self.pad + ((int(pt[0])-1)*x_unit))
            pt[1] = int(self.y1 + self.pad + ((self.y_max - int(pt[1]))*y_unit))

        for pt2 in self.pts2:
            if int(pt2[1]) < 0:
                pt2[1] = 0
            pt2[0] = int(self.x1 + self.pad + ((int(pt2[0])-1)*x_unit))
            pt2[1] = int(self.y1 + self.pad + ((self.y_max - int(pt2[1]))*y_unit))
            
    def axis(self):
        self.x_label = self.font.render(self.x_label+ ",  max:" + str(self.x_max), True, self.black)
        self.y_label = self.font.render(self.y_label + ",  max:" + str(self.y_max), True, self.black)
        
    def draw_graph(self):
        for i in range(len(self.pts1)-1):
            pygame.draw.line(self.screen, self.orange, self.pts1[i], self.pts1[i+1], 2)
            pygame.draw.line(self.screen, self.purple, self.pts2[i], self.pts2[i+1], 2)
            
        self.screen.blit(self.x_label, [self.x1+((self.x2-self.x1)/3), self.y2 -33]) 
        self.screen.blit(self.y_label, [self.x1+3, self.y1+3])
        pygame.draw.rect(self.screen, self.black, self.loc, 2) #border
        pygame.draw.line(self.screen, self.black,
                         [self.x1+self.pad, self.y2-self.pad],
                         [self.x2-self.pad, self.y2-self.pad], 3) #x axis
        pygame.draw.line(self.screen, self.black,
                         [self.x1+self.pad, self.y1+self.pad],
                         [self.x1+self.pad, self.y2-self.pad], 3) #y axis
        
    def run(self):
        self.get_data()
        self.convert()
        self.axis()

def end_game(p1, p2):
    font = pygame.font.SysFont('Arial', 120)
    white = [255,255,255]
    grey = [100, 100, 100]
    black = [0,0,0]
    done = False
    screen = pygame.display.set_mode([1300, 675])
    mana_f = open("mana.txt", "r")
    mana_str = mana_f.read()
    mana_f.close()
    mana_l = mana_str.split()
    mana_l = list(map(int, mana_l))
    print(max(mana_l))
    turn = mana_l[-3]
    del mana_l[::3]
    print(mana_l)
    mana_max = max(mana_l)
    print(mana_max)
    cards_f = open("cards.txt", "r")
    cards_str = cards_f.read()
    cards_f.close()
    cards_l = cards_str.split()
    cards_l = list(map(int, cards_l))
    del cards_l[::3]
    cards_max = max(cards_l)
    health_g = Graph([10,250,400,400],turn,2500,"Turn", "Health", "health.txt", screen) #location, x_max, y_max, x_label, y_label, file, screen
    mana_g = Graph([420,250,400,400],turn,mana_max,"Turn", "Mana", "mana.txt", screen)
    card_g = Graph([850,250,400,400],turn,cards_max,"Turn", "Cards", "cards.txt", screen)
    health_g.run()
    mana_g.run()
    card_g.run()
    if p1.health > p2.health:
        winner = p1.name
    elif p1.health < p2.health:
        winner = p2.name
    else:
        winner = "Nobody"
    congrat = font.render("Congratulations, "+winner+" wins!", True, black)
    
    while not done:
        screen.fill(grey)
        screen.blit(congrat, [25,50])
        health_g.draw_graph()
        mana_g.draw_graph()
        card_g.draw_graph()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                done = True
            elif event.type == pygame.QUIT:
                done = True
            else:
                pass
    screen = pygame.display.set_mode([540, 720]) 
    os.remove(os.path.dirname(sys.argv[0])+"\\player.txt")
    os.remove(os.path.dirname(sys.argv[0])+"\\health.txt")
    os.remove(os.path.dirname(sys.argv[0])+"\\mana.txt")
    os.remove(os.path.dirname(sys.argv[0])+"\\cards.txt")
