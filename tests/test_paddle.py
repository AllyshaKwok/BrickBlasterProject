import unittest
from src.paddle import Paddle


class TestPaddle(unittest.TestCase):
    def setUp(self):
        self.paddle = Paddle(screen_width=600, screen_height=400)

    def test_create_paddle(self):
        self.assertTrue(0 <= self.paddle.xPos <= 600)
        self.assertTrue(0 <= self.paddle.yPos <= 400)
        self.assertGreater(self.paddle.width, 0)

    def test_move_left(self):
        original_x = self.paddle.xPos
        self.paddle.move_left()
        self.assertLess(self.paddle.xPos, original_x)

    def test_move_right(self):
        original_x = self.paddle.xPos
        self.paddle.move_right()
        self.assertGreater(self.paddle.xPos, original_x)


if __name__ == "__main__":
    unittest.main()
