# File created by Dominic Magana
# Sources: Mr. Cozort rps file

import pygame as pg
import random
import sys


# this is for the window settings of the game such as height, width, fps
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
FPS = 30
pg.init()
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# This sets a caption of rock paper scissors
pg.display.set_caption("Rock Paper Scissors")

# this is defining the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# this basically loads the images onto the screen
rps_intro = pg.image.load("rockpapersza.jpg")
rock_img = pg.image.load("rock.jpg")
paper_img = pg.image.load("paper.jpg")
scissors_img = pg.image.load("sza.jpg")

# this basically resizes the images to display them on the screen
rps_intro = pg.transform.scale(rps_intro, (WINDOW_WIDTH, WINDOW_HEIGHT))
rock_img = pg.transform.scale(rock_img, (105, 105))
paper_img = pg.transform.scale(paper_img, (105, 105))
scissors_img = pg.transform.scale(scissors_img, (105, 105))

# the is for the intro of the game
# the "pg.time.wait" is for the time the intro image shows on the screen
def game_intro():
    screen.blit(rps_intro, (0, 0))
    pg.display.update()
    pg.time.wait(2000)

game_intro()

def draw_structure():
    # makes screen black
    screen.fill(BLACK)
    # where the images are placed
    screen.blit(rock_img, (200, 100))
    screen.blit(paper_img, (50, 100))
    screen.blit(scissors_img, (350, 100))

    # This is for the header of screen
    pg.draw.rect(screen, RED, (0, 0, WINDOW_WIDTH, 50))
    header_text = pg.font.Font(None, 36).render("RPS Game", True, WHITE)
    screen.blit(header_text, (WINDOW_WIDTH // 2 - header_text.get_width() // 2, 15))
    instruction = pg.font.Font(None, 30).render("Click on the rock, paper or scissors!",True, GREEN)
    screen.blit(instruction, (WINDOW_WIDTH // 2 - instruction.get_width() // 2, 60))
    pg.display.update()

draw_structure()

# this is for what happends after you click on an image
# this makes it so that it displays that you chose your option based on its positioning
def handle_click(x, y):
    if x > 50 and x < 150 and y > 100 and y < 200:
        display_choice("paper")
        return
    elif x > 200 and x < 300 and y > 100 and y < 200:
        display_choice("rock")
        return
    elif x > 350 and x < 450 and y > 100 and y < 200:
        display_choice("scissors")
        return
    else:
        return

# this is to display what you chose for your option
# it makes it where it will be displayed, what color it will be, and just render it in general
def display_choice(your_choice):
    playmode_font = pg.font.Font(None, 25)
    # display your choice
    your_choice_text = playmode_font.render("You chose: " + your_choice, True, WHITE)
    screen.blit(your_choice_text, (10, 220))

    # This does the same as above, but for what the computer choses
    cpu_choices = random.choice(["rock", "paper", "scissors"])
    cpu_choices_text = playmode_font.render("Computer chose: " + cpu_choices, True, WHITE)
    screen.blit(cpu_choices_text, (200, 220))

    check_winner(your_choice, cpu_choices)

    pg.display.update()

# This code is for the response you get based on what you chose and what the computer choses
def check_winner(your_choice, cpu_choices):
    if your_choice == cpu_choices:
        game_status = "tied! Try Again"
    elif your_choice == "rock":
        if cpu_choices == "paper":
            game_status = "You lost! Paper covers rock."
        else:
            game_status = "You win! Rock crushes scissors."
    elif your_choice == "paper":
        if cpu_choices == "scissors":
            game_status = "You lost! Scissors cuts paper."
        else:
            game_status = "You win! Paper wraps rock."
    elif your_choice == "scissors":
        if cpu_choices == "rock":
            game_status = "You lose! Rock crushes scissors."
        else:
            game_status = "You win! Scissors cuts paper."
    else:
        print("Invalid choice!")
        # renders all of the text after the choice is made
    screen.blit(pg.font.Font(None, 40).render(game_status, True, RED), (10, 275))
    
    # renders the play again button 
    # renders the size of it as well and where it will be on the screen
    playagain_button = pg.Rect(150, 320, 200, 50)
    pg.draw.rect(screen, (173, 89, 29), playagain_button)
    playagain_text = pg.font.Font(None, 30).render("PLAY AGAIN!!!!", True, WHITE)
    screen.blit(playagain_text, (WINDOW_WIDTH // 2 - playagain_text.get_width() // 2, 335))

# this is for the main game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            handle_click(mouse_x, mouse_y)

            # This makes the play again button actually work
            if mouse_x > 150 and mouse_x < 350 and mouse_y > 320 and mouse_y < 370:
                draw_structure()
    pg.time.Clock().tick(FPS)