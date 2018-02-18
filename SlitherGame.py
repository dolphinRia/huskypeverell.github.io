import pygame
import time
import random
pygame.init()

#Declaring Colors
white = (255, 255, 255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 155, 0)

#Displaying the main window
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

#Setting the title
pygame.display.set_caption('Slither')

#Setting the icon
icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)

#Importing the images
img = pygame.image.load('snake_head1.png')
appleimg = pygame.image.load('apple.png')


clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 15

#try making the direction random (idea)
direction = "right"

#Importing fonts
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#Pausing
def pause():

    paused = True
    message_to_screen("Paused", black, -100, size="large")
    message_to_screen("Press C to continue or Q to quit.", black, 25)
    pygame.display.update()
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit
                    quit()
        
        clock.tick(5)

#Keeping score
def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0,0])
    


def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness))#/10.0)*10
    randAppleY = round(random.randrange(0, display_height - AppleThickness))#/10.0)*10

    return randAppleX,randAppleY
  
    
#Start Screen
def game_intro():
    
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither",
                          green,
                          -100,
                          size="large")
        message_to_screen("The objective of the game is to eat red apples",
                          black,
                          -30)
        
        message_to_screen("The more apples you eat, the longer you get",
                          black,
                          10)

        message_to_screen("If you run into yourself or the edges, you die!",
                          black,
                          50)

        message_to_screen("Press C to play, P to pause or Q to quit",
                          black,
                          180)
        
        pygame.display.update()
        clock.tick(5)


    
#Making the snake
def snake(block_size, snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)
        
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
        
    if direction == "up":
        head = img
        
    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()
    
#Allowing messages to be printed to the screen
def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width /2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)

#Actual game
def gameLoop():
    global direction
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()

    #What to do when the game ends
    while not gameExit:

        if gameOver == True:
            message_to_screen("Game Over",
                              red,
                              -50,
                              size="large")
            
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()
            

        while gameOver == True:
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameOver = False
                        gameExit = True
                if event.type == pygame.KEYDOWN:                        
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        direction = "right"
                        gameLoop()
        
        for event in pygame.event.get():
            #If the user presses the X, then quit
            if event.type == pygame.QUIT:
                gameExit = True
                
            #When the arrow keys are pressed, move in that direction    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        #If the user goes out of bounds, quit the program            
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
        
        #Draw and update the frame    
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)

        #Draw the Apple
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))


        #Making the snake head and adjusting the snake body
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        
        snake(block_size, snakeList)
        score(snakeLength - 1)

        
        pygame.display.update()




        # If the snake touches/crosses over the apple make it larger
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()    
                snakeLength += 1
                

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()    
                snakeLength += 1
                

                
        
            
        #frames per second
        clock.tick(FPS)
                
    
    pygame.quit()
    quit()

game_intro()
gameLoop()
