import unittest
from unittest.mock import patch
import pygame
import sys
import os

# Asegúrate de que el directorio src está en el path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import main  # Importar el archivo de tu juego desde la carpeta src

class TestDinosaur(unittest.TestCase):
    @patch('main.pygame.display.set_mode')
    def setUp(self, mock_set_mode):
        # Inicializar el entorno de Pygame y el dinosaurio para las pruebas
        pygame.init()
        self.dino = main.Dinosaur()

    def tearDown(self):
        pygame.quit()

    def test_dinosaur_initial_position(self):
        self.assertEqual(self.dino.dino_rect.x, self.dino.X_POS)
        self.assertEqual(self.dino.dino_rect.y, self.dino.Y_POS)

    def test_dinosaur_duck(self):
        self.dino.dino_duck = True
        self.dino.update()
        self.assertEqual(self.dino.dino_rect.y, self.dino.Y_POS_DUCK)

    def test_dinosaur_run(self):
        self.dino.dino_run = True
        self.dino.update()
        self.assertEqual(self.dino.dino_rect.y, self.dino.Y_POS)

    def test_dinosaur_jump(self):
        self.dino.dino_jump = True
        initial_y = self.dino.dino_rect.y
        self.dino.update()
        self.assertNotEqual(self.dino.dino_rect.y, initial_y)

if __name__ == '__main__':
    unittest.main()
