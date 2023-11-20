import pygame

# pygame setup
pygame.init()
WIDTH, HEIGHT = 500,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.scrap.init()

WHITE, BLACK = (255,255,255), (0,0,0)
STAN_FONT = pygame.font.SysFont("Times New Roman", 15) #STANdard font

FPS = 240

def main():
    global fg_circle_state
    fg_circle_state = False
    clock = pygame.time.Clock()
    fg_circle_cp = (WIDTH/2,HEIGHT/2)
    fg_circle = pygame.draw.circle(WIN,"blue",fg_circle_cp,50)
    counter = 0
    running = True
    while running:
        # poll for events
        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            elif keys_pressed[pygame.K_1] == 1 and fg_circle.collidepoint(pygame.mouse.get_pos()) == True:
                #if mouse is touching joystick and 1 is being held down
                fg_circle_state = True
                if counter == 1:
                    WIN.fill("black")
                    pygame.draw.rect(WIN,WHITE,(0,230,500,40))
                    pygame.draw.rect(WIN,WHITE,(230,0,40,500))
                    counter = 0
                fg_circle_cp == pygame.mouse.get_pos()
                fg_circle = pygame.draw.circle(WIN,"red",pygame.mouse.get_pos(),50)
                counter += 1
                try:
                    output = list(pygame.mouse.get_pos())
                    output1 = output[0]/500
                    output2 = (output[1]/500-1)*-1
                    if output1 < 0.5:
                        output1 = (output1-0.5)
                    else:
                        output1 -= 0.5
                    if output2 < 0.5:
                        output2 = (output2-0.5)
                    else:
                        output2 -= 0.5
                    if round(output1*10000,0) in range(-500,501):
                        output1 = 0
                    if round(output2*10000,0) in range(-500,501):
                        output2 = 0
                except ZeroDivisionError:
                    pass
                output_final = [round(output1,3),round(output2,3)]
            elif keys_pressed[pygame.K_1] != 1 or fg_circle.collidepoint(pygame.mouse.get_pos()) == False:
                fg_circle_state = False
                WIN.fill("black")
                pygame.draw.rect(WIN,WHITE,(0,230,500,40))
                pygame.draw.rect(WIN,WHITE,(230,0,40,500))

        if fg_circle_state == False:
            fg_circle = pygame.draw.circle(WIN,"blue",(WIDTH/2,HEIGHT/2),50)
            output_final = [0,0]
        
        print(output_final)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()