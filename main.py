import pygame
from random import shuffle
import os

import color
import snake

# config
background_color = color.black
edge_color = (0, 153, 153)
snake_head = color.red
snake_body = color.green
snake_tail = color.blue
food_color = (111, 111, 111)
obstacle_color = (255, 115, 0)
image_path = "./assets/images/"

edge_margin = 10
edge_size = 10
screen_margin = edge_margin + edge_size


# sprite
wall = pygame.image.load(os.path.join(image_path, 'wall-36.png'))
background = pygame.image.load(os.path.join(image_path, 'grass-36.png'))
# background = pygame.image.load(os.path.join(image_path, 'plain-36.png'))
food = pygame.image.load(os.path.join(image_path, 'orange-36.png'))
snake_head_icon = pygame.image.load(os.path.join(image_path, 'snake-head-36.png'))
snake_body_line = pygame.image.load(os.path.join(image_path, 'snake-body-line-36.png'))
snake_body_curve = pygame.image.load(os.path.join(image_path, 'snake-body-curve-36.png'))
snake_tail_icon = pygame.image.load(os.path.join(image_path, 'snake-tail-36.png'))

# block
block_width = 36
block_height = 36
col_size = 30
row_size = 20
screen_width = block_width * col_size
screen_height = block_height * row_size
screen = pygame.display.set_mode((screen_width + edge_margin * 4, screen_height + edge_margin * 4))
pygame.display.set_caption('Hong Snake Project')


# render a screen with a screen magin, screen edge, and screen background
def handle_render_screen(screen_width, screen_height):
    screen.fill(color.black)
    pygame.draw.rect(screen, edge_color, (edge_margin, edge_margin, screen_width + edge_margin * 2, screen_height + edge_margin * 2))

    # render background from background color
    # pygame.draw.rect(screen, background_color, (edge_margin + edge_size, edge_margin + edge_size, screen_width, screen_height))

    # render background from background image
    handle_render_background(all_cell)


# render color of a snake
def handle_render_snake(moving_parts):
    # update head
    handle_assign_cell(moving_parts[0], cell_type_dict['snake'])
    handle_draw_cell(snake_head, moving_parts[0][0], moving_parts[0][1])
    handle_draw_cell(snake_body, moving_parts[1][0], moving_parts[1][1])

    # update tail
    if len(moving_parts) > 2:
        handle_draw_cell(snake_tail, moving_parts[2][0], moving_parts[2][1])
        handle_assign_cell(moving_parts[3], cell_type_dict['empty'])
        # replace tail position by background image
        handle_blit_cell(background, moving_parts[3][0], moving_parts[3][1])


# render image of a snake
def handle_render_snake_sprite(snake_position, moving_parts):
    # snake head
    head_degree = 0
    if snake_position[0][2] == 'W':
        head_degree = 0
    elif snake_position[0][2] == 'S':
        head_degree = 180
    elif snake_position[0][2] == 'A':
        head_degree = 90
    elif snake_position[0][2] == 'D':
        head_degree = -90

    handle_assign_cell(moving_parts[0], cell_type_dict['snake'])
    temp = pygame.transform.rotate(snake_head_icon, head_degree)
    handle_blit_cell(temp, moving_parts[0][0], moving_parts[0][1])
    
    # snake body
    if snake_position[0][2] == snake_position[1][2]:
        body_degree = 0
        if snake_position[1][2] == 'W' or snake_position[1][2] == 'S':
            body_degree = 0
        else:
            body_degree = 90
        temp = pygame.transform.rotate(snake_body_line, body_degree)
        handle_blit_cell(temp, moving_parts[1][0], moving_parts[1][1])
    else:
        body_degree = 0
        if snake_position[0][2] == 'W' and snake_position[1][2] == 'D':
            body_degree = 0
        elif snake_position[0][2] == 'A' and snake_position[1][2] == 'S':
            body_degree = 0
        elif snake_position[0][2] == 'A' and snake_position[1][2] == 'W':
            body_degree = 90
        elif snake_position[0][2] == 'S' and snake_position[1][2] == 'D':
            body_degree = 90
        elif snake_position[0][2] == 'W' and snake_position[1][2] == 'A':
            body_degree = -90
        elif snake_position[0][2] == 'D' and snake_position[1][2] == 'S':
            body_degree = -90
        elif snake_position[0][2] == 'D' and snake_position[1][2] == 'W':
            body_degree = 180
        elif snake_position[0][2] == 'S' and snake_position[1][2] == 'A':
            body_degree = 180

        temp = pygame.transform.rotate(snake_body_curve, body_degree)
        handle_blit_cell(temp, moving_parts[1][0], moving_parts[1][1])

    # snake tail
    if len(moving_parts) > 2:

        tail_degree = 0
        if snake_position[-2][2] == 'W':
            tail_degree = 0
        elif snake_position[-2][2] == 'S':
            tail_degree = 180
        elif snake_position[-2][2] == 'A': 
            tail_degree = 90
        elif snake_position[-2][2] == 'D':
            tail_degree = -90

        temp = pygame.transform.rotate(snake_tail_icon, tail_degree)
        handle_blit_cell(temp, moving_parts[2][0], moving_parts[2][1])


        handle_assign_cell(moving_parts[3], cell_type_dict['empty'])
        handle_blit_cell(background, moving_parts[3][0], moving_parts[3][1])


# render a screen background
def handle_render_background(all_cell):
    for cell in all_cell:
        handle_blit_cell(background, cell[0], cell[1])


# render a obstacles
def handle_render_obstacle(obstacles):
    for obstacle in obstacles:
        # obstacle in color
        # handle_draw_cell(obstacle_color, obstacle[0], obstacle[1])

        # obstacle in image
        handle_blit_cell(wall, obstacle[0], obstacle[1])


# render a food
def handle_render_food():
    temp = all_cell.copy()
    shuffle(temp)
    point = None
    for cell in temp:
        if (get_cell(cell) == 0):
            point = cell

    if point != None:
        handle_assign_cell(point, cell_type_dict['food'])
        # draw food by color
        # handle_draw_cell(food_color, point[0], point[1])

        # draw food by image
        handle_blit_cell(food, point[0], point[1])


# draw image in the specify XY coordinates
def handle_blit_cell(image, cell_col, cell_row):
    screen.blit(image, 
        (cell_col * block_width + screen_margin,
        cell_row * block_height + screen_margin))


# fill the cell in the specify XY coordinates
def handle_draw_cell(color, cell_col, cell_row):
    pygame.draw.rect(screen, color, (
        cell_col * block_width + screen_margin,
        cell_row * block_height + screen_margin,
        block_width, 
        block_height))


# assign the value of the grid cell which will be used to check wether the cell is empty of contains a snake, a food, or an obstacle
def handle_assign_cell(point, value):
    x = point[0]
    y = point[1]
    grid_map[y][x] = value


# check wether the given point is out of the screen or not
def check_in_range(point, col_size, row_size):
    return (0 <= point[0] and point[0] < col_size) and (0 <= point[1] and point[1] < row_size)


# handle the object when it is going out the screen by placed it in the another side of the screen
def handle_object_move_out_screen(point, col_size, row_size):
    x, y, moving_direction = point
    if x < 0:
        x = col_size - 1
    elif x >= col_size:
        x = 0
    elif y < 0:
        y = row_size - 1
    elif y >= row_size:
        y = 0

    return [x, y, moving_direction]


# get the cell by given the specific point
def get_cell(point):
    return grid_map[point[1]][point[0]]


# handle grid
# each cell represents a object in the grid map
cell_type_dict = {
    'empty': 0,
    'snake': 1,
    'obstacle': 2,
    'food': 3
}
grid_map = [[0 for col in range(0, col_size)] for row in range(0, row_size)]
all_cell = []
for x in range(0, col_size):
    for y in range(0, row_size):
        all_cell.append([x, y])

# construct wall - array of position (x, y) = (col, row)
obstacles = []
for x in range(0, col_size):
    for y in range(0, row_size):
        if (x == 0 or x == col_size-1) or (y == 0 or y == row_size-1):
            # all bourdary cell
            # obstacles.append([x, y])
            # handle_assign_cell([x, y], cell_type_dict['obstacle'])

            # make some hole for moving through the screen
            if (y < row_size/2 -1 or y > row_size/2 + 1):
                obstacles.append([x, y])
                handle_assign_cell([x, y], cell_type_dict['obstacle'])


# create a snake
initial_length = 5
moving_direction = 'D'
initial_position = [col_size//2, row_size//2, moving_direction]
my_snake = snake.Snake(moving_direction, initial_position, initial_length)


handle_render_screen(screen_width, screen_height)
handle_render_obstacle(obstacles)
handle_render_food()
running = True
while running:

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # handle event from user
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

    # peak next position
    snake_head_position = my_snake.get_next_head_position()
    snake_head_position[2] = moving_direction

    # if snake move out of screen, it will be placed in the other side of the screen
    if not check_in_range(snake_head_position, col_size, row_size):
        snake_head_position = handle_object_move_out_screen(snake_head_position, col_size, row_size)

    # get the cell that a snake is moving to
    cell = get_cell(snake_head_position)

    remove_tail = True
    drop_food = False
    if cell == 1: # snake meet itself and goes crash
        running = False
    elif cell == 2: # snake hit with an obstacle (a wall)
        running = False
    elif cell == 3: # snake found a food and grow (length longer)
        drop_food = True
        remove_tail = False


    moving_parts = my_snake.move(snake_head_position, remove_tail)

    # render snake with sprite
    handle_render_snake_sprite(my_snake.get_location(), moving_parts)

    if drop_food:
        handle_render_food()


    # update map
    pygame.display.update()
    pygame.time.delay(70)
