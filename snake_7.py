import pygame
import time
import random
pygame.init()

screen = pygame.display.set_mode((1000, 650))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake game - by Sarah Kan")

# Tuples containing the colours to be used in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (188, 227, 199)
yellow = (255, 255, 0)

# Fonts for the game
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

clock = pygame.time.Clock()  # sets the speed at which the snake moves

def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Centre rectangle: 1200/2 = 650 and 650/2 = 330
    text_box = txt.get_rect(center=(500, 310))
    screen.blit(txt, text_box)


# Function to run the main game loop
def game_loop():
    quit_game = False
    game_over = False

    # snake will be 20 x 20 pixels
    snake_x = 490  # Centre point horizontally is (1200-20 snake width)/2 = 640
    snake_y = 350  # Centre point vertically is (660-20 snake width)/2 = 315

    snake_x_change = 0  # holds the value of changes in the x-coordinate
    snake_y_change = 0  # holds hte value of changes in the y-coordinate

    # Setting a random position for the food - to start
    food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
    food_y = round(random.randrange(20, 620 - 20) / 20) * 20

    while not quit_game:
        # Give user the option to quit or play again when they die
        while game_over:
            screen.fill(white)
            message("You died! Press 'Q' to Quit or 'A' to play Again", black, white)
            pygame.display.update()

            # Check if user wants to quit or play again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()  # Restart the main game loop

        # other
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = "Exit: X to Quit, SPACE to resume, R to reset"
                message(instructions, white, black)
                pygame.display.update()

                end = False
                while not end:
                    for event in pygame.event.get():
                        # If user presses X button, game quits
                        if event.type == pygame.QUIT:
                            quit_game = True
                            end = True

                        # If user presses 'R' button again, game is reset
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                end = True, game_loop()

                        # If user presses the space-bar, game continues
                            if event.key == pygame.K_SPACE:
                                end = True

                        # If user presses 'Q' game quits
                            if event.key == pygame.K_q:
                                quit_game = True
                                end = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -20
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = 20
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_x_change = 0
                    snake_y_change = -20
                elif event.key == pygame.K_DOWN:
                    snake_x_change = 0
                    snake_y_change = 20
        if snake_x >= 1000 or snake_x < 0 or snake_y >= 620 or snake_y < 0:
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green)  # Changes screen (surface) from default black to green

        # Create rectangle for snake
        pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
        pygame.display.update()

        # Create circle for food
        pygame.draw.circle(screen, yellow, [food_x, food_y], 10)
        pygame.display.update()

        # Collision detection (test if snake touches food)
        if snake_x == food_x - 10 and snake_y == food_y - 10:
            # Set new random position for food if snake touches it
            food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
            food_y = round(random.randrange(20, 620 - 20) / 20) * 20

        clock.tick(5)  # sets the speed at which each iteration of the game loop
        # runs in frames per second(fps). In this case it is set to 5fps

    pygame.quit()
    quit()

# Main routine
game_loop()
