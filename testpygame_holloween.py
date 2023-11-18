import unittest
from unittest import TestCase
import pygame
import pygame_holloween

class TestGameFunctions(TestCase):

    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_yellow_movement(self):
        yellow = pygame.Rect(100, 300, pygame_holloween.GHOST_WIDTH, pygame_holloween.GHOST_HEIGHT)
        keys_pressed = {pygame.K_a: True, pygame.K_d: False, pygame.K_w: False, pygame.K_s: False}
        pygame_holloween.yellow_handle_movement(keys_pressed, yellow)
        self.assertEqual(yellow.x, 95)  # The ghost should have moved 5 units to the left

    def test_red_movement(self):
        red= pygame.Rect(100, 300, pygame_holloween.GHOST_WIDTH, pygame_holloween.GHOST_HEIGHT)
        keys_pressed = {pygame.K_a: True, pygame.K_d: False, pygame.K_w: False, pygame.K_s: False}
        pygame_holloween.yellow_handle_movement(keys_pressed, red)
        self.assertEqual(red.x, 95)  # The ghost should have moved 5 units to the left
    
    def test_handle_bullets(self):
        yellow = pygame.Rect(100, 300,pygame_holloween.GHOST_WIDTH, pygame_holloween.GHOST_HEIGHT)
        red = pygame.Rect(700, 300,pygame_holloween.GHOST_WIDTH, pygame_holloween.GHOST_HEIGHT)
        yellow_bullets = [pygame.Rect(110, 302, 10, 5)]
        red_bullets = [pygame.Rect(700, 302, 10, 5)]
    
    
if __name__ == '__main__':
    unittest.main()
