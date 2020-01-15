import pygame #, winsound

def skip():
    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.mixer.music.stop()
            else:
                pass

def tutorial():
    #pygame.event.pump

    tut_pics = []
    for i in range(19):
        tut_pics.append(pygame.image.load("tut"+str(i+1)+".png"))
    for i in range (2, 6):
        pygame.mixer.music.load("audio"+str(i)+".wav")
        pygame.mixer.music.play(0, 0)
        skip()
    screen = pygame.display.set_mode([1300, 675])
    for i in range(19):
        screen.blit(tut_pics[i], [0,0])
        pygame.display.flip()
        pygame.mixer.music.load("audio"+str(i+6)+".wav")
        pygame.mixer.music.play(0, 0)
        skip()

        #winsound.PlaySound("audio"+str(i)+".wav", winsound.SND_FILENAME)
####
####    screen.blit(tut_pics[0], [0,0])
####    pygame.display.flip()
####    winsound.PlaySound("audio6.wav", winsound.SND_FILENAME)
####    screen.blit(tut_pics[1], [0,0])
####    pygame.display.flip()
####    winsound.PlaySound("audio7.wav", winsound.SND_FILENAME)
####    screen.blit(tut_pics[2], [0,0])
####    pygame.display.flip()
####    winsound.PlaySound("audio8.wav", winsound.SND_FILENAME)
####    screen.blit(tut_pics[3], [0,0])
####    pygame.display.flip()
####    winsound.PlaySound("audio9.wav", winsound.SND_FILENAME)
####    screen.blit(tut_pics[4], [0,0])
####    pygame.display.flip()
####    winsound.PlaySound("audio10.wav", winsound.SND_FILENAME)
####    screen.blit(tut_pics[5], [0,0])
####    pygame.display.flip()
####    winsound.PlaySound("audio11.wav", winsound.SND_FILENAME)
 #   screen.blit(tut_pics[6], [0,0])
 #   pygame.display.flip()
##    pygame.event.pump
##    winsound.PlaySound("audio12.wav", winsound.SND_FILENAME)
##    pygame.event.pump
##    screen.blit(tut_pics[7], [0,0])
##    pygame.display.flip()
##    winsound.PlaySound("audio13.wav", winsound.SND_FILENAME)
##    pygame.event.pump
##    screen.blit(tut_pics[8], [0,0])
##    pygame.display.flip()
##    winsound.PlaySound("audio14.wav", winsound.SND_FILENAME)
##    pygame.event.pump
##    screen.blit(tut_pics[9], [0,0])
##    pygame.display.flip()
##    winsound.PlaySound("audio15.wav", winsound.SND_FILENAME)
##    pygame.event.pump
#    pygame.mixer.music.load("audio12.wav")
#    pygame.mixer.music.play(0, 0)
#    while pygame.mixer.music.get_busy():
#        for event in pygame.event.get():
#            pass
    screen = pygame.display.set_mode([540, 720])
#pygame.quit()
