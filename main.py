import pygame
import color
import snake

max_width = 1000    
max_height = 800
screen = pygame.display.set_mode((max_width, max_height))
pygame.display.set_caption('Hong Snake Ja')

running = True
clock = pygame.time.Clock()
frame_per_second = 60

# block
block_width = 20
block_height = 20

initial_length = 5
initial_position = [10, 10]
moving_direction = 'D'
my_snake = snake.Snake(moving_direction, initial_position, initial_length)

screen.fill(color.white)
count = 1
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == ord('w')) and moving_direction != 'S':
                moving_direction = 'W'
            elif (event.key == pygame.K_DOWN or event.key == ord('s')) and moving_direction != 'W':
                moving_direction = 'S'
            elif (event.key == pygame.K_LEFT or event.key == ord('a')) and moving_direction != 'D':
                moving_direction = 'A'
            elif (event.key == pygame.K_RIGHT or event.key == ord('d')) and moving_direction != 'A':
                moving_direction = 'D'


    ## moving snake
    my_snake.set_moving_direction(moving_direction)

    moving_parts = my_snake.move()

    # next_head
    pygame.draw.rect(screen, color.red, (moving_parts[0][0] * block_width, moving_parts[0][1] * block_height, block_width, block_height))

    # prev_head
    pygame.draw.rect(screen, color.green, (moving_parts[1][0] * block_width, moving_parts[1][1] * block_height, block_width, block_height))

    # update tail
    if len(moving_parts) > 2:
        # next_tail
        pygame.draw.rect(screen, color.blue, (moving_parts[2][0] * block_width, moving_parts[2][1] * block_height, block_width, block_height))

        # prev_tail
        # same color as background
        pygame.draw.rect(screen, color.white, (moving_parts[3][0] * block_width, moving_parts[3][1] * block_height, block_width, block_height))


    pygame.display.update()
    pygame.time.delay(70)
