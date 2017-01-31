import pygame
# pygame import
pygame.init()
# initialize the game engine

#def colors():
BLACK 	=(0,0,0)
WHITE	=(255,255,255)
RED		=(255,0,0)
GREEN	=(0,255,0)
BLUE	=(0,0,255)

#def variables():
PI = 3.141592653

size = (700,500) # screen size
screen = pygame.display.set_mode(size) # opens the display
pygame.display.set_caption("pyTempest") # adds window title

#colors()
#variables()

# Loop until the user click the close button
done = False

# used to manage game ticks
clock = pygame.time.Clock()

# -------- Main Program Loop ---------
while not done:
	#----- Main Event Loop --------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("User asked to quit.")
			done = True #closes game by stopping loop
		elif event.type == pygame.KEYDOWN:
			print("User pressed a key.")
		elif event.type == pygame.KEYUP
			print("User let go of a key.")
		elif event.type == pygame.MOUSEBUTTONDOWN
			print("User pressed a mouse button.")


	# --- Game Logic goes here

	# --- Drawing code goes here

	#first, clear the screen to white. Don't put other drawing
	#commands above this, or they will be erased with this command
	screen.fill(WHITE);

	# --- Go ahread and update the screen with what we've drawn
	pygame.display.flip()

	# --- Limit to 60 fps
	clock.tick(60)

#proper shutdown
pygame.quit()

exit()