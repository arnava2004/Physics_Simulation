import pygame, sys, pymunk #importing modules

def create_mass(space):
    mass = pymunk.Body(1,100,body_type = pymunk.Body.DYNAMIC)
    mass.position = (400, 0)
    shape = pymunk.Circle(mass,80)
    space.add(mass,shape)
    return shape

def draw_masses(masses):
    for mass in masses:
        pos_x = int(mass.body.position.x)
        pos_y = int(mass.body.position.y)
        pygame.draw.circle(screen,(0,0,0), (pos_x,pos_y), 80)
pygame.init()
screen = pygame.display.set_mode((800,800)) #setting screen size
clock = pygame.time.Clock() # making game clock
space = pymunk.Space()
space.gravity = (0,500)

masses = []
masses.append(create_mass(space))

while True: #overall loop for game
    for event in pygame.event.get():#user input
        if event.type == pygame.QUIT: # if we get the input to close game
            pygame.quit()
            sys.exit()

    screen.fill((217, 217, 217)) #color (white)
    draw_masses(masses)
    space.step(1/50)
    pygame.display.update() # update screen
    clock.tick(120) # frames per second is 120
