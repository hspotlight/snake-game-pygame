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

edge_margin = 10
edge_size = 10
screen_margin = edge_margin + edge_size


# block
block_width = 36
block_height = 36
col_size = 30
row_size = 20
screen_width = block_width * col_size
screen_height = block_height * row_size
screen = pygame.display.set_mode((screen_width + edge_margin * 4, screen_height + edge_margin * 4))
pygame.display.set_caption('Hong Snake Project')

all_cell = []
for x in range(0, col_size):
    for y in range(0, row_size):
        all_cell.append([x, y])

# food
food = None

def handle_render_screen(screen_width, screen_height):
    screen.fill(color.black)
    pygame.draw.rect(screen, edge_color, (edge_margin, edge_margin, screen_width + edge_margin * 2, screen_height + edge_margin * 2))
    pygame.draw.rect(screen, background_color, (edge_margin + edge_size, edge_margin + edge_size, screen_width, screen_height))


def handle_render_snake(moving_parts):
    # update head
    handle_assign_cell(moving_parts[0], 1)
    handle_draw_cell(snake_head, moving_parts[0][0], moving_parts[0][1])
    handle_draw_cell(snake_body, moving_parts[1][0], moving_parts[1][1])

    # update tail
    if len(moving_parts) > 2:
        handle_draw_cell(snake_tail, moving_parts[2][0], moving_parts[2][1])
        handle_assign_cell(moving_parts[3], 0)
        handle_draw_cell(background_color, moving_parts[3][0], moving_parts[3][1])


def handle_render_background(all_cell):
    for cell in all_cell:
        handle_blit_cell(wall, cell[0], cell[1])

def handle_render_obstacle(obstacles):
    for obstacle in obstacles:
        # obstacle in color
        handle_draw_cell(obstacle_color, obstacle[0], obstacle[1])


def handle_render_food():
    temp = all_cell.copy()
    shuffle(temp)
    point = None
    for cell in temp:
        if (get_cell(cell) == 0):
            point = cell

    if point != None:
        food = point
        handle_assign_cell(point, 3)
        handle_draw_cell(food_color, point[0], point[1])


# draw image in the specify XY coordinates
def handle_blit_cell(image, cell_col, cell_row):
    screen.blit(image, 
        (cell_col * block_width + screen_margin,
        cell_row * block_height + screen_margin))


def handle_draw_cell(color, cell_col, cell_row):
    pygame.draw.rect(screen, color, (
        cell_col * block_width + screen_margin,
        cell_row * block_height + screen_margin,
        block_width, 
        block_height))


def handle_assign_cell(point, value):
    x = point[0]
    y = point[1]
    grid_map[y][x] = value


def check_in_range(point, col_size, row_size):
    return (0 <= point[0] and point[0] < col_size) and (0 <= point[1] and point[1] < row_size)


def handle_object_move_out_screen(point, col_size, row_size):
    x, y = point
    if x < 0:
        x = col_size - 1
    elif x >= col_size:
        x = 0
    elif y < 0:
        y = row_size - 1
    elif y >= row_size:
        y = 0

    return [x, y]


def get_cell(point):
    return grid_map[point[1]][point[0]]


# handle grid
# each cell represents a object in the grid map
# 0 = empty
# 1 = snake
# 2 = obstacle
# 3 = food
grid_map = [[0 for col in range(0, col_size)] for row in range(0, row_size)]

# construct wall - array of position (x, y) = (col, row)
obstacles = []
for x in range(0, col_size):
    for y in range(0, row_size):
        if (x == 0 or x == col_size-1) or (y == 0 or y == row_size-1):
            # all bourdary cell
            # obstacles.append([x, y])
            # handle_assign_cell([x, y], 2)

            # make some hole for moving through the screen
            if (y < row_size/2 -1 or y > row_size/2 + 1):
                obstacles.append([x, y])
                handle_assign_cell([x, y], 2)


# create a snake
initial_length = 15
initial_position = [int(col_size/2), int(row_size/2)]
moving_direction = 'D'
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

    # if snake move out of screen, it will be placed in the other side of the screen
    if not check_in_range(snake_head_position, col_size, row_size):
        snake_head_position = handle_object_move_out_screen(snake_head_position, col_size, row_size)

    cell = get_cell(snake_head_position)

    remove_tail=True
    drop_food=False
    if cell == 1: # snake itself
        running = False
    elif cell == 2: # obstacle
        running = False
    elif cell == 3: # food
        # create new food
        drop_food = True
        remove_tail = False


    moving_parts = my_snake.move(snake_head_position, remove_tail)
    handle_render_snake(moving_parts)

    if drop_food:
        handle_render_food()


    # update map
    pygame.display.update()
    pygame.time.delay(70)
