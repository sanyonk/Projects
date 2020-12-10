import pygame
from pygame.locals import *

class Control:
	def __init__(self):
		self.flag_game = True
		self.flag_direction = "RIGHT"

	def control(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.flag_game = False
			elif event.type == KEYDOWN:
				if event.key == K_RIGHT:
					self.flag_direction = "RIGHT"
				elif event.key == K_LEFT:
					self.flag_direction = "LEFT"
				if event.key == K_UP:
					self.flag_direction = "UP"
				elif event.key == K_DOWN:
					self.flag_direction = "DOWN"
				elif event.key == K_ESCAPE:
					self.flag_direction = False