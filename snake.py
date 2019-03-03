class Snake:
    def __init__(self, moving_direction, point, initial_length=5):
        self.moving_direction = moving_direction
        self.location = [point]
        self.initial_length = initial_length

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

    def set_moving_direction(self, moving_direction):
        self.moving_direction = moving_direction

    # return the moving parts of the snake includes next head, current head, and previous tail
    # output = (head_next, head_prev, tail_next?, tail_prev?)
    def move(self):
        head_next = self.get_next_head_position()
        head_prev = self.get_current_head_position()

        output = [head_next, head_prev]
        if len(self.location) >= self.initial_length and len(self.location) >= 2:
            tail_prev = self.location.pop()
            tail_next = self.location[-1]
            output.append(tail_next)
            output.append(tail_prev)

        self.location.insert(0, head_next)
        return output
