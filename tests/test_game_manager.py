import unittest
from src.brick import Brick
from src.paddle import Paddle
from src.ball import Ball, BigBall
from src.game_manager import GameManager


class TestGameManager(unittest.TestCase):
    def setUp(self):
        self.manager = GameManager(screen_width=600, screen_height=400)

    def test_ball_paddle_collision(self):
        self.manager.ball.yPos = self.manager.paddle.yPos - self.manager.ball.radius
        self.manager.ball.xPos = self.manager.paddle.xPos
        collided = self.manager.check_ball_paddle_collision(self.manager.ball, self.manager.paddle)
        self.assertTrue(collided)

    def test_ball_brick_collision(self):
        test_brick = Brick(250, 100)
        self.manager.bricks.append(test_brick)
        self.manager.ball.xPos = test_brick.xPos
        self.manager.ball.yPos = test_brick.yPos
        self.manager.check_ball_brick_collision(self.manager.ball)
        self.assertTrue(test_brick.is_destroyed)

    def test_lose_condition(self):
        self.manager.balls.clear()
        self.assertTrue(self.manager.check_loss())

    def test_win_condition(self):
        for brick in self.manager.bricks:
            brick.is_destroyed = True
        self.assertTrue(self.manager.check_win())


if __name__ == "__main__":
    unittest.main()