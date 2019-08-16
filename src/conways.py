import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 500
TOTAL_SQUARES = 400

cur_states = [0] * TOTAL_SQUARES
cur_states[30] = 1
cur_states[31] = 1
cur_states[32] = 1
cur_states[49] = 1
cur_states[50] = 1
cur_states[51] = 1
# cur_states[70] = 1
# cur_states[71] = 1
# cur_states[69] = 1
#cur_states[90] = 1
next_states = [0] * TOTAL_SQUARES


# sample square = 50
square_index = 50




pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    for i in range(TOTAL_SQUARES):
        square_index = i
    # check all neigbors and get the total live count
    # Define the locations of the neighbors
        width = 20
        south = square_index + width
        north = square_index - width
        east = square_index + 1
        west = square_index - 1
        north_east = square_index - width + 1
        north_west = square_index - width - 1
        south_east = square_index + width + 1
        south_west = square_index + width - 1
    
        neighbors_list = [north, south, east, west, north_west, north_east, south_west, south_east]

        live_neighbor_count = 0
    # add up live neighbors
        for neighbor in neighbors_list:
            if neighbor >= 0 and neighbor < 400:
                if cur_states[neighbor] == 1:
                    live_neighbor_count += 1
        if square_index == 30 or square_index == 50 or square_index == 70 or square_index == 49 or square_index == 51:
            print("index is ", square_index, "neighbor count is ", live_neighbor_count)
    # IMPLEMENT THE RULES
    # for each square check its neighbors and update its state based on the rules
    # - _birth_ - a "dead" cell with exactly 3 live neighbors will "come to life"
        if cur_states[square_index] == 0 and live_neighbor_count == 3:
            next_states[square_index] = 1


    #- _life_ - a "live" cell with exactly 2 or 3 live neighbors will "stay alive"
        if cur_states[square_index] == 1 and ( live_neighbor_count == 2 or live_neighbor_count == 3 ):
            next_states[square_index] = 1

    #- _death_ - a "live" cell with a single OR 4+ live neighbors will "die"
        if cur_states[square_index] == 1 and ( live_neighbor_count == 1 or live_neighbor_count >= 4 ):
            next_states[square_index] = 0

        if square_index == 30 or square_index == 50 or square_index == 70 or square_index == 49 or square_index == 51:
            print("next state is ", next_states[square_index])

        

    print(cur_states)
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
    color = BLACK
    sqr_index = 0
    # --- Drawing code should go here
    for i in range(20):
        for j in range(20):
            if cur_states[sqr_index] == 1:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(screen, color, pygame.Rect(j*20 + 5*j, i*20 + 5*i, 20, 20))
            sqr_index += 1
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
    cur_states = next_states
    next_states = [0] * TOTAL_SQUARES

    #print(next_states)
 
# Close the window and quit.
pygame.quit()
