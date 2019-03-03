class Snake:
    # initial the properties of a snake
    def __init__(self, moving_direction, point, initial_length=5):
        self.moving_direction = moving_direction
        self.location = [point]
        self.initial_length = initial_length


    # get the next position of the snake according to its moving direction
    # note that this function is only used for peak where the snake is going to
    def get_next_head_position(self):

        # get current head position
        next_head_position = self.get_current_head_position()
        direction = self.moving_direction
        if direction == 'W':
            next_head_position[1] -= 1
        if direction == 'S':
            next_head_position[1] += 1
        if direction == 'A':
            next_head_position[0] -= 1
        if direction == 'D':
            next_head_position[0] += 1

        return next_head_position

    def get_current_head_position(self):
        return self.location[0].copy()

    # set the moving direction of the snake from an event triggered by user or other object
    def set_moving_direction(self, moving_direction):
        self.moving_direction = moving_direction


    def get_moving_direction(self):
        return self.moving_direction


    # return the moving parts of the snake includes next head, current head, and previous tail
    # output = (head_next, head_prev, tail_next?, tail_prev?)
    def move(self, next_head_position, remove_tail=True):
        head_next = next_head_position
        head_prev = self.get_current_head_position()

        output = [head_next, head_prev]
        if remove_tail and len(self.location) >= self.initial_length and len(self.location) >= 2:
            tail_prev = self.location.pop()
            tail_next = self.location[-1]
            output.append(tail_next)
            output.append(tail_prev)

        self.location.insert(0, head_next)
        return output

    def get_location(self):
        return self.location