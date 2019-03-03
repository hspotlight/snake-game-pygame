import pygame
import color

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

# create a snake

def get_next_head_position():
    # move one block at a time
    next_head_position = point[0].copy()
    if moving_direction == 'W':
        next_head_position[1] -= 1
    if moving_direction == 'S':
        next_head_position[1] += 1
    if moving_direction == 'A':
        next_head_position[0] -= 1
    if moving_direction == 'D':
        next_head_position[0] += 1
    return next_head_position



initial_length = 30
initial_position = [10, 10]
moving_direction = 'D'
point = []
point.append(initial_position)

temp_initial_length = initial_length

screen.fill(color.white)
count = 1
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # get key and change direction
            if (event.key == pygame.K_UP or event.key == ord('w')) and moving_direction != 'S':
            # if event.key == pygame.K_UP:
                moving_direction = 'W'
            elif (event.key == pygame.K_DOWN or event.key == ord('s')) and moving_direction != 'W':
            # elif event.key == pygame.K_DOWN:
                moving_direction = 'S'
            elif (event.key == pygame.K_LEFT or event.key == ord('a')) and moving_direction != 'D':
            # elif event.key == pygame.K_LEFT:
                moving_direction = 'A'
            elif (event.key == pygame.K_RIGHT or event.key == ord('d')) and moving_direction != 'A':
            # elif event.key == pygame.K_RIGHT:
                moving_direction = 'D'

    # move snake position according to the direction
    next_head_position = get_next_head_position()
    last_head_position = point[0]
    pygame.draw.rect(screen, color.green, (last_head_position[0] * block_width, last_head_position[1] * block_height, block_width, block_height))

    point.insert(0, next_head_position)
    # print(next_head_position)
    pygame.draw.rect(screen, color.red, (next_head_position[0] * block_width, next_head_position[1] * block_height, block_width, block_height))

    if (temp_initial_length == 0):
        tail_position = point.pop()
        # print(tail_position)
        pygame.draw.rect(screen, color.white, (tail_position[0] * block_width, tail_position[1] * block_height, block_width, block_height))
    else:
        temp_initial_length -= 1

    pygame.display.update()

    # clock.tick(frame_per_second)
    # print('hello')
    # print(count)
    # count += 1
    pygame.time.delay(70)
