import pygame

WHITE = (255, 255, 255)

class Ball:
	MAX_VEL = 8
	COLOR = WHITE

	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius
		self.x_vel = self.MAX_VEL
		self.y_vel = 0

	def draw(self, win):
		pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)
	
	def move(self):
		self.x += self.x_vel
		self.y += self.y_vel