from pygame import mixer
mixer.init()

HEIGHT = 500

def handle_collisions(ball, player, wall):
	if ball.y + ball.radius >= HEIGHT:
		boundary_sound = mixer.Sound("data/Assets/Audio/BoundaryCollide.wav")
		boundary_sound.play()
		ball.y_vel *= -1
	elif ball.y - ball.radius <= 0:
		boundary_sound = mixer.Sound("data/Assets/Audio/BoundaryCollide.wav")
		boundary_sound.play()
		ball.y_vel *= -1
	
	if ball.x_vel < 0:
		if ball.y >= player.y and ball.y <= player.y + player.height and ball.x - ball.radius <= player.x + player.width:
			paddle_sound = mixer.Sound('data/Assets/Audio/PaddleColide.wav')
			paddle_sound.play()
			ball.x_vel *= -1

			middle_y = player.y + player.height/2
			diffrence_in_y = middle_y - ball.y
			reduction_factor = (player.height/2) / ball.MAX_VEL
			y_vel = diffrence_in_y / reduction_factor
			ball.y_vel = -1 * y_vel

	else:
		if ball.y >= wall.y and ball.y <= wall.y + wall.height and ball.x + ball.radius >= wall.x:
			wall_sound = mixer.Sound("data/Assets/Audio/WallCollide.wav")
			wall_sound.play()
			ball.x_vel *= -1

			middle_y = wall.y + wall.height/2
			diffrence_in_y = middle_y - ball.y
			reduction_factor = (wall.height/2) / ball.MAX_VEL
			y_vel = diffrence_in_y / reduction_factor
			ball.y_vel = -1 * y_vel