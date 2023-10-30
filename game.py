# importing all the necessary packages to make this simple game
import pygame
import time
import random

pygame.font.init()


# stating the dimensions of the screen in pixels
WIDTH, HEIGHT = 1000, 800
# making the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# setting the caption for the window
pygame.display.set_caption("loller😂🤣💀😆👽")

#    loading the image into the script (not acutally drawing it on screen)
# however if you want the image to scale to the width and the height you can do this :
BG = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT))
# BG = pygame.image.load("background.jpg")

# defining the dimensions of the player
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

# defining the dimensions of the star
STAR_WIDTH = 10
STAR_HEIGHT = 20
# defining the player velocity
PLAYER_VEL = 5
# defining the star velocity
STAR_VEL = 3

# font, font type and the size of the font
FONT = pygame.font.SysFont("Times New Roman", 30)


def draw(player, elapsed_time, stars):
    # the command 'blit' is used to draw smth on the screen
    # the 0, 0 stands for where the top left of the img will be placed
    WIN.blit(BG, (0, 0))

    # drawing the elasped time
    # round the time, 1 stands for anti alysing and white is the colour of the font
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")

    # rendering this ^^^  on the screen
    # blit the time_text and the coords is 10, 10 smth like padding
    WIN.blit(time_text, (10, 10))

    # drawing the rectangle
    # pygame.draw.rect(where you want to draw the player, what colour you want it to be, what you want to draw)
    pygame.draw.rect(WIN, "blue", player)

    # drawin the stars
    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    # this will just refrsh/update the display to draw necessary changes
    pygame.display.update()


# now that we have the whole screen set up, we need a loop to keep the game running so something sort of like a while loop.
# the while loop will do things like check for collsion for movement and key presses and will adust what is on the screen

# this is the function called 'main' where the game logic is going to exist
def main():
    # this is to show if the game is running or now
    # true means the game is running, false means the game will quit
    run = True

    # player = pygame.Rect(x coord, y coord, player width, player height)
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    # defining the clock object
    clock = pygame.time.Clock()

    # keeping track of time
    # this line over here is going to give us the current time
    start_time = time.time()
    # defing the elapsed time variable
    elapsed_time = 0

    # the first star will be added after 2000 milliseconds
    star_add_increment = 2000
    # var that tells us when we should add the next star
    star_count = 0

    # where we are going to store all of our different stars that are currently on the screen
    stars = []
    # defining hit
    hit = False

    # while the variable run = true
    while run:

        # returning the amount of milliseconds that have occured since the last clock tick
        # 60 frames per second only, so the character does not move that fast
        star_count += clock.tick(60)

        # storing what time you are starting the while loop at
        # gives the no. of secs that have elapsed since the whle loop
        elapsed_time = time.time() - start_time

        # if the star count is greater than the 2000 milliseconds then...
        if star_count > star_add_increment:
            # for placeholder in the range 3 so 3 stars
            for _ in range(3):
                # pick a random integer from the width of the screen
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                # for the y coord (2nd one), it is -star height because it will look like its entering the screen.
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                # putting this into the stars list
                stars.append(star)

            # setting the star_add_increment to some time less so that stars are deployed faster
            # 50 milliseconds will get removed until 200 milliseconds
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        # this is a list of all the events that have occured in the last iteration of the game
        # for example: mouse clicks, buttons pressed will be recorded
        for event in pygame.event.get():
            # if the button 'X' on the top right hand corner is pressed...
            if event.type == pygame.QUIT:
                # set run to false and break out of this for loop
                run = False
                break

        # moving the rectangle with arrow keys

        # gives the dictionary of all the keys that the user has pressed
        keys = pygame.key.get_pressed()

        # changing the x coord by +5 or -5 depending if you pressed the left or right arrow
        # and checking that the x coord is greater than 0 (means you are still in the window)
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        # moving the stars
        # making a copy of the stars list so we can remove the stars from the list that have touched the bottom of the screen
        for star in stars[:]:
            star.y += STAR_VEL
            # if the stars y level is greater than of the screen (it has gone out of the screen) then remove the star
            if star.y > HEIGHT:
                stars.remove(star)
            # to see if the star is collinding with the player
            # then to set hit = Ture and break out of the loop
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        # if hit = true
        if hit:
            lost_text = FONT.render(f"ni hao:{round(elapsed_time)}s", 1, "white")
            # draw the text in the centre of the screen
            WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
            # since i am not doing this in the draw function, I  have to manually update the screen
            pygame.display.update()
            # delay this for 4 secs
            pygame.time.delay(4000)
            # end the game
            break

        # running the draw function
        draw(player, elapsed_time, stars)

    # quitting the game window
    pygame.quit()


# If you are running the Python file directly, the main() function will be executed.
# If you are importing the Python file from another Python file, the main() function will not be executed.
if __name__ == "__main__":
    main()
