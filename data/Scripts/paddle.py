import pygame

WHITE = (255, 255, 255)

class Paddle:
	COLOR = WHITE
	VEL = 7

	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	
	def draw(self, win):
		pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))
	
	def move_up(self):
		self.y -= self.VEL
	
	def move_down(self):
		self.y += self.VEL