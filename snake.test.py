import unittest
from snake import Snake

class TestSnake(unittest.TestCase):
	def setUp(self):
		col_size = 30
		row_size = 20
		initial_length = 5
		moving_direction = 'D'
		initial_position = [col_size // 2, row_size // 2, moving_direction]
		self.snake = Snake(moving_direction, initial_position, initial_length)

	def tearDown(self):
		pass

	def test_snake_should_have_correct_position(self):
		snake_position = self.snake.get_current_head_position()[:2]
		self.assertEqual(snake_position,[19,10])

	def test_snake_should_move_to_next_position_correctly(self):
		directions = 'WASD'
		next_position = [
			[19,9],
			[18,10],
			[19,11],
			[20,10]
		]
		snake = self.snake
		for i in range(4):
			snake.set_moving_direction(directions[i])
			snake_next_position = snake.get_next_head_position()[:2]
			self.assertEqual(snake_next_position,next_position[i])

	def test_snake_should_move(self):
		directions = 'WASD'
		snake = self.snake
		for d in directions:
			snake.set_moving_direction(d)
			next_position = snake.get_next_head_position()
			snake.move(snake.get_next_head_position())
			self.assertEqual(
				snake.get_current_head_position(),
				next_position
			)

if __name__ == '__main__':
	unittest.main()