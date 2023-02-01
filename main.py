import pygame
from pygame import mixer
import math
import os
import time
import random
from sys import exit
from data.Scripts.paddle import Paddle
from data.Scripts.wall import Wall
from data.Scripts.ball import Ball
from data.Scripts.collisions import handle_collisions
pygame.init()
mixer.init()

#Variables
WIDTH, HEIGHT = 500, 500
FPS = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
BALL_RADIUS = 10
SCORE_FONT = pygame.font.Font("data/Fonts/PublicPixel.ttf", 100)

if os.path.exists('score.txt'):
	with open('score.txt', 'r') as file:
		high_score = int(file.read())
else:
	high_score = 0

pygame.display.set_caption("One Player Pong")

mixer.music.load("data/Assets/Audio/BG.wav")

def draw(win, paddle, wall, ball, score):
	win.fill(BLACK)
	score_text = SCORE_FONT.render(f"{score}", 1, (171, 171, 171))
	win.blit(score_text, (WIDTH//2 - score_text.get_width()//2 - paddle.x, HEIGHT//2 - score_text.get_height()//2))
	paddle.draw(win)
	wall.draw(win)
	ball.draw(win)

def load_img(path, screen, x, y):
	img = pygame.image.load(path).convert_alpha()
	screen.blit(img, (x,y))

def splash_screen():
	clock = pygame.time.Clock()
	run = True

	while run:
		SCREEN.fill((0,0,0))
		load_img("data/Assets/Images/Main.png", SCREEN, 0, 0)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				exit()
		
		pygame.display.update()
		clock.tick(FPS)
		pygame.time.wait(700)
		main_menu()
	pygame.quit()
	exit()

def main_menu():
	clock = pygame.time.Clock()
	run = True

	mixer.music.play(-1)
	mixer.music.set_volume(0.2)

	while run:
		t = pygame.time.get_ticks()/5
		y1 = math.sin(t/50)*30
		SCREEN.fill((0,0,0))
		load_img("data/Assets/Images/Title.png", SCREEN, 0, y1)
		load_img("data/Assets/Images/Start.png", SCREEN, 0, 0)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					game()

		pygame.display.update()
		clock.tick(FPS)
	pygame.quit()
	exit()

def game():
	run = True
	clock = pygame.time.Clock()

	mixer.music.set_volume(0.1)

	global score, high_score
	score = 0
	paddle_y = random.randint(10, 390)

	player = Paddle(10, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
	wall = Wall(WIDTH - PADDLE_WIDTH, 0, PADDLE_WIDTH, HEIGHT)
	ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)

	while run:
		draw(SCREEN, player, wall, ball, score)
		
		keys = pygame.key.get_pressed()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				exit()
		
		if (keys[pygame.K_UP] or keys[pygame.K_w]) and player.y - player.VEL >= 0:
			player.move_up()
		if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.y + player.height + player.VEL <= HEIGHT:
			player.move_down()
	
		ball.move()
		handle_collisions(ball, player, wall)

		if ball.y >= player.y and ball.y <= player.y + player.height and ball.x - ball.radius <= player.x + player.width:
			score+=1
		elif ball.x < 0:
			player.VEL = 0
			ball.x_vel = 0
			ball.y_vel = 0
			if score > high_score:
				high_score = score
				with open('data/Scripts/highscore.txt', 'w') as file:
					file.write(str(high_score))
			gameover_sound = mixer.Sound("data/Assets/Audio/GameOver.wav")
			gameover_sound.play()
			time.sleep(2)
			game_over()

		pygame.display.update()
		clock.tick (FPS)
	pygame.quit()
	exit()

def game_over():
	clock = pygame.time.Clock()
	run = True
	FONT2 = pygame.font.Font("data/Fonts/PublicPixel.ttf", 41)
	FONT3 = pygame.font.Font("data/Fonts/PublicPixel.ttf", 35)

	mixer.music.set_volume(0.2)

	while run:

		SCREEN.fill((0,0,0))
		scoretext = FONT2.render(f"{score}", 1, WHITE)
		SCREEN.blit(scoretext, (365, 210))
		highscoretext = FONT3.render(f"{high_score}", 1, WHITE)
		SCREEN.blit(highscoretext, (370, 285))

		load_img("data/Assets/Images/Game Over.png", SCREEN, 0, 0)
		load_img("data/Assets/Images/Score.png", SCREEN, 0, 0)
		load_img("data/Assets/Images/High Score.png", SCREEN, 0, 0)
		load_img("data/Assets/Images/Restart.png", SCREEN, 0, 0)
		load_img("data/Assets/Images/Quit.png", SCREEN, 0, 0)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					game()
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					exit()

		pygame.display.update()
		clock.tick(FPS)
	pygame.quit()
	exit()

splash_screen()