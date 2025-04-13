import unittest
from src.ball import Ball, BigBall


class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(screen_width=600, screen_height=400)
        self.big_ball = BigBall(screen_width=600, screen_height=400)

    def test_create_ball(self):
        self.assertTrue(0 <= self.ball.xPos <= 600)
        self.assertTrue(0 <= self.ball.yPos <= 400)
        self.assertNotEqual(self.ball.speed_x, 0)
        self.assertNotEqual(self.ball.speed_y, 0)

    def test_create_big_ball(self):
        self.assertTrue(0 <= self.big_ball.xPos <= 600)
        self.assertTrue(0 <= self.big_ball.yPos <= 400)
        self.assertGreater(self.big_ball.radius, self.ball.radius)


if __name__ == "__main__":
    unittest.main()