import pygame
pygame.init()

screen = pygame.display.set_mode((1300, 650))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake game - by Sarah Kan")

# Tuples containing the colours to be used in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (188, 227, 199)

# Fonts for the game
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)

clock = pygame.time.Clock()  # sets the speed at which the snake moves

quit_game = False

# snake will be 20 x 20 pixels
snake_x = 640  # Centre point horizontally is (1300-20 snake width)/2 = 640
snake_y = 315  # Centre point vertically is (650-20 snake width)/2 = 315

snake_x_change = 0  # holds the value of changes in the x-coordinate
snake_y_change = 0  # holds hte value of changes in the y-coordinate

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

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

    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(green)  # Changes screen (surface) from default black to green

    # Create rectangle for snake
    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    clock.tick(5) # sets teh speed at which each iteration of the game loop
    # runs in frames per second(fps). In this case it is set to 5fps

pygame.quit()
quit()

