import unittest
from src.brick import Brick, MegaBrick, SpawningBrick, IndestructibleBrick, PowerUpBrick


class TestBrick(unittest.TestCase):
    def test_spawn_brick(self):
        test_brick = Brick(0, 0)
        self.assertIsNotNone(test_brick)
        self.assertEqual(test_brick.xPos, 0)
        self.assertEqual(test_brick.yPos, 0)

    def test_create_mega_brick(self):
        brick = MegaBrick(100, 50)
        self.assertEqual(brick.health, 2)

    def test_create_spawning_brick(self):
        brick = SpawningBrick(200, 60)
        self.assertTrue(brick.spawns_extra_ball)

    def test_create_indestructible_brick(self):
        brick = IndestructibleBrick(300, 70)
        self.assertFalse(brick.is_destroyed)

    def test_create_powerup_brick(self):
        powerup_brick = PowerUpBrick(150, 80)
        self.assertTrue(powerup_brick.gives_powerup)


if __name__ == "__main__":
    unittest.main()