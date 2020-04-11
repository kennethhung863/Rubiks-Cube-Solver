#  test
# Author: Kenneth Hung
# This is the file that runs the solver, and displays the cube graphically using PyGame
# Currently under testing and refining, but still functional
#   



# Import and initialize the pygame library
import pygame
import sys
import math
from rectangle import rectangle
from square import square
from button import button
import rubiks_solver
import random

import time


# colors
white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
orange = ((255,150,0))
yellow = ((255,255,0))

black = ((0,0,0))
gray = ((192,192,192))
background_color = ((170,225,240))











pygame.init()
surface = pygame.display.set_mode([1000, 600])
pygame.display.set_caption('Rubik\'s Cube Solver') 
surface.fill(background_color)







def display_text(surface, color, x, y, size, str):

    font = pygame.font.SysFont('Calibri', size) 
    
    # create a text suface object, 
    # on which text is drawn on it. 
    text = font.render(str, True, color) 
    textRect = text.get_rect()  
    
    # set the center of the rectangular object. 
    textRect.center = (x, y) 
    surface.blit(text, textRect) 


def cube_to_graphics(cube, graphics_cube):
    for s in range(0,6):
        for i in range(0,3):
            for j in range(0,3):
                graphics_cube[s][i][j].color = char_to_color(cube[s][i][j])

def graphics_to_cube(cube, graphics_cube):
    for s in range(0,6):
        for i in range(0,3):
            for j in range(0,3):
                cube[s][i][j] = color_to_char(graphics_cube[s][i][j].color)

def char_to_color(char):
    if char == 'b':
        return blue
    elif char == 'r':
        return red
    elif char == 'g':
        return green
    elif char == 'o':
        return orange
    elif char == 'y':
        return yellow
    elif char == 'w':
        return white
    else:
        return black  

def color_to_char(color):
    if color == blue:
        return 'b'
    elif color == red:
        return 'r'
    elif color == green:
        return 'g'
    elif color == orange:
        return 'o'
    elif color == yellow:
        return 'y'
    elif color == white:
        return 'w'
    else:
        return ' '   

# generating 9 squares for 1 side. x and y is position of TOP LEFT corner
def side(color, x, y, width):
    # 3x3 2D array - inserting 9 squares into the sides
    square_tile = []
    for i in range(0,3):
        temp = []
        for j in range(0,3):
            temp.append(square(surface, color, (x+(width*j)), (y+(width*i)), width))
        square_tile.append(temp)
    
    graphics_cube.append(square_tile)
    
# testing prints
def print_side(side):
    for i in range(0,3):
            print(side[i])

def print_cube(cube):
    for i in range(0,6):
            print_side(cube[i])
            print()

# cube movements
def up():
    print('U')
    #making new list to copy
    temp_left = []
    for i in range(0,3):
        temp_left.append(char_cube[0][i][:])
    temp_front = []
    for i in range(0,3):
        temp_front.append(char_cube[1][i][:])
    temp_right = []
    for i in range(0,3):
        temp_right.append(char_cube[2][i][:])
    temp_back = []
    for i in range(0,3):
        temp_back.append(char_cube[3][i][:])
    temp_up = []
    for i in range(0,3):
        temp_up.append(char_cube[5][i][:])

    # rotate up
    for i in range(0,3):
        for j in range(0,3):
            char_cube[5][i][j] = temp_up[2-j][i]
    
    # left side replace
    for i in range(0,3):
        char_cube[0][0][i] = temp_front[0][i]
    # front side replace
    for i in range(0,3):
        char_cube[1][0][i] = temp_right[0][i]
    # right side replace
    for i in range(0,3):
        char_cube[2][0][i] = temp_back[0][i]
    # back side replace
    for i in range(0,3):
        char_cube[3][0][i] = temp_left[0][i]

    update_cube()

def up_prime():
    print('U\'')

    #making new list to copy
    temp_left = []
    for i in range(0,3):
        temp_left.append(char_cube[0][i][:])
    temp_front = []
    for i in range(0,3):
        temp_front.append(char_cube[1][i][:])
    temp_right = []
    for i in range(0,3):
        temp_right.append(char_cube[2][i][:])
    temp_back = []
    for i in range(0,3):
        temp_back.append(char_cube[3][i][:])
    temp_down = []
    for i in range(0,3):
        temp_down.append(char_cube[4][i][:])
    temp_up = []
    for i in range(0,3):
        temp_up.append(char_cube[5][i][:])

    # rotate up
    for i in range(0,3):
        for j in range(0,3):
            char_cube[5][i][j] = temp_up[j][2-i]
    
    # left side replace
    for i in range(0,3):
        char_cube[0][0][i] = temp_back[0][i]
    # front side replace
    for i in range(0,3):
        char_cube[1][0][i] = temp_left[0][i]
    # right side replace
    for i in range(0,3):
        char_cube[2][0][i] = temp_front[0][i]
    # back side replace
    for i in range(0,3):
        char_cube[3][0][i] = temp_right[0][i]
    update_cube()

def down():
    print('D')

    #making new list to copy
    temp_left = []
    for i in range(0,3):
        temp_left.append(char_cube[0][i][:])
    temp_front = []
    for i in range(0,3):
        temp_front.append(char_cube[1][i][:])
    temp_right = []
    for i in range(0,3):
        temp_right.append(char_cube[2][i][:])
    temp_back = []
    for i in range(0,3):
        temp_back.append(char_cube[3][i][:])
    temp_down = []
    for i in range(0,3):
        temp_down.append(char_cube[4][i][:])  
    temp_up = []
    for i in range(0,3):
        temp_up.append(char_cube[5][i][:])

    # rotate down
    for i in range(0,3):
        for j in range(0,3):
            char_cube[4][i][j] = temp_down[2-j][i]
    
    # left side replace
    for i in range(0,3):
        char_cube[0][2][i] = temp_back[2][i]
    # front side replace
    for i in range(0,3):
        char_cube[1][2][i] = temp_left[2][i]
    # right side replace
    for i in range(0,3):
        char_cube[2][2][i] = temp_front[2][i]
    # back side replace
    for i in range(0,3):
        char_cube[3][2][i] = temp_right[2][i]
    update_cube()

def down_prime():
    print('D\'')

    #making new list to copy
    temp_left = []
    for i in range(0,3):
        temp_left.append(char_cube[0][i][:])
    temp_front = []
    for i in range(0,3):
        temp_front.append(char_cube[1][i][:])
    temp_right = []
    for i in range(0,3):
        temp_right.append(char_cube[2][i][:])
    temp_back = []
    for i in range(0,3):
        temp_back.append(char_cube[3][i][:])
    temp_down = []
    for i in range(0,3):
        temp_down.append(char_cube[4][i][:])  
    temp_up = []
    for i in range(0,3):
        temp_up.append(char_cube[5][i][:])

    # rotate down
    for i in range(0,3):
        for j in range(0,3):
            char_cube[4][i][j] = temp_down[j][2-i]
    
    # left side replace
    for i in range(0,3):
        char_cube[0][2][i] = temp_front[2][i]
    # front side replace
    for i in range(0,3):
        char_cube[1][2][i] = temp_right[2][i]
    # right side replace
    for i in range(0,3):
        char_cube[2][2][i] = temp_back[2][i]
    # back side replace
    for i in range(0,3):
        char_cube[3][2][i] = temp_left[2][i]
    update_cube()

def left():
    print('L')

    #making new list to copy
    temp_left = []
    for i in range(0,3):
        temp_left.append(char_cube[0][i][:])
    temp_front = []
    for i in range(0,3):
        temp_front.append(char_cube[1][i][:])
    temp_right = []
    for i in range(0,3):
        temp_right.append(char_cube[2][i][:])
    temp_back = []
    for i in range(0,3):
        temp_back.append(char_cube[3][i][:])
    temp_down = []
    for i in range(0,3):
        temp_down.append(char_cube[4][i][:])  
    temp_up = []
    for i in range(0,3):
        temp_up.append(char_cube[5][i][:])
  

    # rotate left
    for i in range(0,3):
        for j in range(0,3):
            char_cube[0][i][j] = temp_left[2-j][i]
    
    # back side replace
    for i in range(0,3):
        char_cube[3][i][2] = temp_down[2-i][0]
    # up side replace
    for i in range(0,3):
        char_cube[5][i][0] = temp_back[2-i][2]
    # front side replace
    for i in range(0,3):
        char_cube[1][i][0] = temp_up[i][0]
    # bottom side replace
    for i in range(0,3):
        char_cube[4][i][0] = temp_front[i][0]
    update_cube()

def left_prime():
    print('L\'')

    #making new list to copy
    temp_left = []
    for i in range(0,3):
        temp_left.append(char_cube[0][i][:])
    temp_front = []
    for i in range(0,3):
        temp_front.append(char_cube[1][i][:])
    temp_right = []
    for i in range(0,3):
        temp_right.append(char_cube[2][i][:])
    temp_back = []
    for i in range(0,3):
        temp_back.append(char_cube[3][i][:])
    temp_down = []
    for i in range(0,3):
        temp_down.append(char_cube[4][i][:])  
    temp_up = []
    for i in range(0,3):
        temp_up.append(char_cube[5][i][:])
  

    # rotate left
    for i in range(0,3):
        for j in range(0,3):
            char_cube[0][i][j] = temp_left[j][2-i]
    
    # back side replace
    for i in range(0,3):
        char_cube[3][i][2] = temp_up[2-i][0]
    # up side replace
    for i in range(0,3):
        char_cube[5][i][0] = temp_front[i][0]
    # front side replace
    for i in range(0,3):
        char_cube[1][i][0] = temp_down[i][0]
    # bottom side replace
    for i in range(0,3):
        char_cube[4][i][0] = temp_back[2-i][2]
    update_cube()

def right():
    print('R')

    #making new list to copy
    temp_left = []
    for i in range(0,3):
        temp_left.append(char_cube[0][i][:])
    temp_front = []
    for i in range(0,3):
        temp_front.append(char_cube[1][i][:])
    temp_right = []
    for i in range(0,3):
        temp_right.append(char_cube[2][i][:])
    temp_back = []
    for i in range(0,3):
        temp_back.append(char_cube[3][i][:])
    temp_down = []
    for i in range(0,3):
        temp_down.append(char_cube[4][i][:])  
    temp_up = []
    for i in range(0,3):
        temp_up.append(char_cube[5][i][:])
  

    # rotate left
    for i in range(0,3):
        for j in range(0,3):
            char_cube[2][i][j] = temp_right[2-j][i]
    
    # back side replace
    for i in range(0,3):
        char_cube[3][i][0] = temp_up[2-i][2]
    # up side replace
    for i in range(0,3):
        char_cube[5][i][2] = temp_front[i][2]
    # front side replace
    for i in range(0,3):
        char_cube[1][i][2] = temp_down[i][2]
    # bottom side replace
    for i in range(0,3):
        char_cube[4][i][2] = temp_back[2-i][0]
    update_cube()

def right_prime():
    print('R\'')

    #making new list to copy
    temp_left = []
    for i in range(0,3):
        temp_left.append(char_cube[0][i][:])
    temp_front = []
    for i in range(0,3):
        temp_front.append(char_cube[1][i][:])
    temp_right = []
    for i in range(0,3):
        temp_right.append(char_cube[2][i][:])
    temp_back = []
    for i in range(0,3):
        temp_back.append(char_cube[3][i][:])
    temp_down = []
    for i in range(0,3):
        temp_down.append(char_cube[4][i][:])  
    temp_up = []
    for i in range(0,3):
        temp_up.append(char_cube[5][i][:])
  

    # rotate right
    for i in range(0,3):
        for j in range(0,3):
            char_cube[2][i][j] = temp_right[j][2-i]
    
    # back side replace
    for i in range(0,3):
        char_cube[3][i][0] = temp_down[2-i][2]
    # up side replace
    for i in range(0,3):
        char_cube[5][i][2] = temp_back[2-i][0]
    # front side replace
    for i in range(0,3):
        char_cube[1][i][2] = temp_up[i][2]
    # bottom side replace
    for i in range(0,3):
        char_cube[4][i][2] = temp_front[i][2]
    update_cube()

def front():
    print('F')

    #making new list to copy
    temp_left = []
    for i in range(0,3):
        temp_left.append(char_cube[0][i][:])
    temp_front = []
    for i in range(0,3):
        temp_front.append(char_cube[1][i][:])
    temp_right = []
    for i in range(0,3):
        temp_right.append(char_cube[2][i][:])
    temp_back = []
    for i in range(0,3):
        temp_back.append(char_cube[3][i][:])
    temp_down = []
    for i in range(0,3):
        temp_down.append(char_cube[4][i][:])  
    temp_up = []
    for i in range(0,3):
        temp_up.append(char_cube[5][i][:])
  

    # rotate front
    for i in range(0,3):
        for j in range(0,3):
            char_cube[1][i][j] = temp_front[2-j][i]
    
    # left side replace
    for i in range(0,3):
        char_cube[0][i][2] = temp_down[0][i]
    # up side replace
    for i in range(0,3):
        char_cube[5][2][i] = temp_left[2-i][2]
    # right side replace
    for i in range(0,3):
        char_cube[2][i][0] = temp_up[2][i]
    # bottom side replace
    for i in range(0,3):
        char_cube[4][0][i] = temp_right[2-i][0]
    update_cube()

def front_prime():
    print('F\'')

    #making new list to copy
    temp_left = []
    for i in range(0,3):
        temp_left.append(char_cube[0][i][:])
    temp_front = []
    for i in range(0,3):
        temp_front.append(char_cube[1][i][:])
    temp_right = []
    for i in range(0,3):
        temp_right.append(char_cube[2][i][:])
    temp_back = []
    for i in range(0,3):
        temp_back.append(char_cube[3][i][:])
    temp_down = []
    for i in range(0,3):
        temp_down.append(char_cube[4][i][:])  
    temp_up = []
    for i in range(0,3):
        temp_up.append(char_cube[5][i][:])
  

    # rotate front
    for i in range(0,3):
        for j in range(0,3):
            char_cube[1][i][j] = temp_front[j][2-i]
    
    # left side replace
    for i in range(0,3):
        char_cube[0][i][2] = temp_up[2][2-i]
    # up side replace
    for i in range(0,3):
        char_cube[5][2][i] = temp_right[i][0]
    # right side replace
    for i in range(0,3):
        char_cube[2][i][0] = temp_down[0][2-i]
    # bottom side replace
    for i in range(0,3):
        char_cube[4][0][i] = temp_left[i][2]
    update_cube()

def back():
    print('B')

    #making new list to copy
    temp_left = []
    for i in range(0,3):
        temp_left.append(char_cube[0][i][:])
    temp_front = []
    for i in range(0,3):
        temp_front.append(char_cube[1][i][:])
    temp_right = []
    for i in range(0,3):
        temp_right.append(char_cube[2][i][:])
    temp_back = []
    for i in range(0,3):
        temp_back.append(char_cube[3][i][:])
    temp_down = []
    for i in range(0,3):
        temp_down.append(char_cube[4][i][:])  
    temp_up = []
    for i in range(0,3):
        temp_up.append(char_cube[5][i][:])
  

    # rotate back
    for i in range(0,3):
        for j in range(0,3):
            char_cube[3][i][j] = temp_back[2-j][i]
    
    # up side replace
    for i in range(0,3):
        char_cube[0][i][0] = temp_up[0][2-i]
    # right side replace
    for i in range(0,3):
        char_cube[5][0][i] = temp_right[i][2]
    # down side replace
    for i in range(0,3):
        char_cube[2][i][2] = temp_down[2][2-i]
    # left side replace
    for i in range(0,3):
        char_cube[4][2][i] = temp_left[i][0]
    update_cube()

def back_prime():
    print('B\'')

    #making new list to copy
    temp_left = []
    for i in range(0,3):
        temp_left.append(char_cube[0][i][:])
    temp_front = []
    for i in range(0,3):
        temp_front.append(char_cube[1][i][:])
    temp_right = []
    for i in range(0,3):
        temp_right.append(char_cube[2][i][:])
    temp_back = []
    for i in range(0,3):
        temp_back.append(char_cube[3][i][:])
    temp_down = []
    for i in range(0,3):
        temp_down.append(char_cube[4][i][:])  
    temp_up = []
    for i in range(0,3):
        temp_up.append(char_cube[5][i][:])
  

    # rotate back
    for i in range(0,3):
        for j in range(0,3):
            char_cube[3][i][j] = temp_back[j][2-i]
    
    # down side replace
    for i in range(0,3):
        char_cube[0][i][0] = temp_down[2][i]
    # left side replace
    for i in range(0,3):
        char_cube[5][0][i] = temp_left[2-i][0]
    # up side replace
    for i in range(0,3):
        char_cube[2][i][2] = temp_up[0][i]
    # right side replace
    for i in range(0,3):
        char_cube[4][2][i] = temp_right[2-i][2]  
    update_cube()

def rotate_cw():
    print('Rotate CW')
    #making new list to copy
    temp_left = []
    for i in range(0,3):
        temp_left.append(char_cube[0][i][:])
    temp_front = []
    for i in range(0,3):
        temp_front.append(char_cube[1][i][:])
    temp_right = []
    for i in range(0,3):
        temp_right.append(char_cube[2][i][:])
    temp_back = []
    for i in range(0,3):
        temp_back.append(char_cube[3][i][:])
    temp_down = []
    for i in range(0,3):
        temp_down.append(char_cube[4][i][:])  
    temp_up = []
    for i in range(0,3):
        temp_up.append(char_cube[5][i][:])

    # rotate up
    for i in range(0,3):
        for j in range(0,3):
            char_cube[5][i][j] = temp_up[2-j][i]

    # rotate down
    for i in range(0,3):
        for j in range(0,3):
            char_cube[4][i][j] = temp_down[j][2-i]

    for i in range(0,3):
        for j in range(0,3):
            char_cube[0][i][j] = temp_front[i][j]
            char_cube[1][i][j] = temp_right[i][j]
            char_cube[2][i][j] = temp_back[i][j]
            char_cube[3][i][j] = temp_left[i][j]
    update_cube()
def rotate_ccw():
    print("Rotate CCW (3x Rotate CW)")
    for i in range(0,3):
        rotate_cw()
# graphics update functions
def update_cube():
    #time.sleep(0.1)
    cube_to_graphics(char_cube, graphics_cube)
    draw()

def draw():
    # side squares
    for s in range(0,6):
        for i in range(0,3):
            for j in range(0,3):
                graphics_cube[s][i][j].draw()
        
        # grid line using top left square coordinates
        x = graphics_cube[s][0][0].x
        y = graphics_cube[s][0][0].y
        width = graphics_cube[s][0][0].width
        for line in range(0,4):
            pygame.draw.rect(surface, black, (x-2, ((y-2)+(line*width)), (3*width + 2), 2))
            pygame.draw.rect(surface, black, (((x-2)+(line*width)), y-2, 2, (3*width + 2)))
    
    # buttons
    if not(solving):
        start_button.draw()
        rotate_cw_button.draw()
        scramble_button.draw()
        test_button.draw()
        up_button.draw()
        up_prime_button.draw()
        front_button.draw()
        front_prime_button.draw()
        down_button.draw()
        down_prime_button.draw()
        left_button.draw()
        left_prime_button.draw()
        right_button.draw()
        right_prime_button.draw()
        back_button.draw()
        back_prime_button.draw()

    # title
    display_text(surface, black, 150, 100, 30, 'Rubik\'s Cube Solver')
    pygame.display.update()

def scramble():
    print('scrambling')
    shuffles = random.randint(25,30)
    for i in range(0, shuffles):
        turn = random.randint(0,11)
        if turn == 0:
            up()
        elif turn == 1:
            up_prime()
        elif turn == 2:
            down()
        elif turn == 3:
            down_prime()
        elif turn == 4:
            left()
        elif turn == 5:
            left_prime()
        elif turn == 6:
            front()
        elif turn == 7:
            front_prime()
        elif turn == 8:
            right()
        elif turn == 9:
            right_prime()
        elif turn == 10:
            back()
        else:
            back_prime()

def test():
    for i in range(0,200):
        scramble()
        solve()
        box = rectangle(surface, white, 180, 480, 40, 40)
        box.draw()
        display_text(surface, black, 200, 500, 30, str((i+1)))


# solving algorithm
def solve():
    print("solving...")
    # initially assume unsolved
    solve_stage = 1
    # run until it is solved
    # change this later to max states+1
    solve_stage_counter = 0
    infinite = False
    while solve_stage != 9:
        prev_solve_stage = solve_stage

        solve_stage = run_solve_stage(solve_stage)
        print_cube(char_cube)

        if prev_solve_stage == solve_stage:
            solve_stage_counter += 1
        else:
            solve_stage_counter = 0

        if solve_stage_counter > 40:
            print("infinite loop at stage ",solve_stage)
            infinite = True

        assert(not(infinite))

    assert(is_cube_solved())

    print('finished solving')
    

def run_solve_stage(solve_stage):
    # different stages of the solving process: next stage is updated every time a solve algorithm runs
    # change this to add the rest of the states
    if solve_stage == 1:
        solve_stage = solve_cross_unordered(solve_stage)
    elif solve_stage == 2:        
        solve_stage = solve_cross_complete(solve_stage)
    elif solve_stage == 3:
        solve_stage = solve_second_layer(solve_stage)
    elif solve_stage == 4:
        solve_stage = solve_white_corners(solve_stage)
    elif solve_stage == 5:
        solve_stage = solve_yellow_cross(solve_stage)
    elif solve_stage == 6:
        solve_stage = solve_yellow_side(solve_stage)
    elif solve_stage == 7:
        solve_stage = solve_last_layer(solve_stage)
    elif solve_stage == 8:
        solve_stage = solve_last_layer_middle(solve_stage)
    return solve_stage

#stage 4: solve white corners
# Rotate CW
# Rotate CW
# Rotate CW
# Rotate CW
# Rotate CW
# Rotate CW
# Rotate CW
# Rotate CW
# ['w', 'r', 'w']
# ['r', 'r', 'r']
# ['y', 'r', 'y']

# ['r', 'y', 'o']
# ['g', 'g', 'g']
# ['b', 'g', 'b']

# ['w', 'y', 'g']
# ['o', 'o', 'o']
# ['y', 'o', 'r']

# ['w', 'o', 'r']
# ['b', 'b', 'b']
# ['y', 'b', 'g']

# ['o', 'w', 'r']
# ['w', 'w', 'w']
# ['o', 'w', 'g']

# ['g', 'y', 'o']
# ['y', 'y', 'g']
# ['b', 'b', 'b']


def solve_cross_unordered(solve_stage):
    print('stage 1: cross unordered')
    # are the side pieces in place
    if  char_cube[4][0][1] == 'w' and char_cube[4][1][0] == 'w' and char_cube[4][1][2] == 'w' and char_cube[4][2][1] == 'w':
        print('stage 1 solved')
        solve_stage = 2
        return solve_stage


    elif solve_stage == 1:
        print('solving stage 1')
        # check top of cube
        for s in range(0,4):
            if (char_cube[5][2][1] == 'w' and not(char_cube[4][0][1] == 'w')):
                print('found a piece on top, rotating F2 to place')
                front()
                front()
            elif (char_cube[5][2][1] == 'w' and (char_cube[4][0][1] == 'w')):
                print('found a piece on top, but it is being blocked')
                while char_cube[4][0][1] == 'w':
                    down()
                    print('rotating to unblock')
                print('placing piece on top')
                front()
                front()
            print('next piece')
            rotate_cw()
        
            # check for left, front, right and back
        for s in range(0,4):
            # top side
            if char_cube[1][0][1] == 'w' and not(char_cube[4][0][1] == 'w'):
                front()
            elif char_cube[1][0][1] == 'w' and (char_cube[4][0][1] == 'w'):
                while char_cube[4][0][1] == 'w':
                    down()
                front()
            
            # bottom side
            if char_cube[1][2][1] == 'w' and not(char_cube[4][0][1] == 'w'):
                front()

            rotate_cw()


        # check for left, front, right and back on left and right side
        for s in range(0,4):
            # left side
            if char_cube[1][1][0] == 'w' and not(char_cube[4][1][0] == 'w'):
                left()
            elif char_cube[1][1][0] == 'w' and (char_cube[4][1][0] == 'w'):
                while char_cube[4][1][0] == 'w':
                    down()
                left()
            
            # right side
            if char_cube[1][1][2] == 'w' and not(char_cube[4][1][2] == 'w'):
                right()
            elif char_cube[1][1][2] == 'w' and (char_cube[4][1][2] == 'w'):
                while char_cube[4][1][2] == 'w':
                    down()
                right()
            rotate_cw()
        return solve_stage

    else:
        print("error at stage 1")
        return None

def solve_cross_complete(solve_stage):
    print('stage 2: cross complete')

    if char_cube[0][2][1] == char_cube[0][1][1] and char_cube[1][2][1] == char_cube[1][1][1] and char_cube[2][2][1] == char_cube[2][1][1] and char_cube[3][2][1] == char_cube[3][1][1]:
        print('stage 2 solved')
        solve_stage = 3
        return solve_stage   
    # make flower pattern
    elif solve_stage == 2:
        front()
        front()
        left()
        left()
        back()
        back()
        right()
        right()


        for s in range(0,4):
            while not(char_cube[1][0][1] == char_cube[1][1][1]):
                up_prime()
                rotate_cw()
            front()
            front()
            rotate_cw()
        solve_stage = 3
        return solve_stage

    else:
        print("error at stage 2")
        return None    

def solve_second_layer(solve_stage):
    print('stage 3: solve second layer')

    second_layer_solved = True
    # check if it is solved
    for s in range(0,4):
        for i in range(0,3):
            if not(char_cube[s][1][i] == char_cube[s][1][1]):
                second_layer_solved = False
    if second_layer_solved == True:
        solve_stage = 4
        return solve_stage

    #rotate algorithm to place

    for s in range(0,4):
        #if there is a side piece on the top, orient it so then it matches center then place
        for t in range(0,4):
            if char_cube[1][0][1] == char_cube[1][1][1]:
                # put up to left
                if char_cube[5][2][1] == char_cube[0][1][1]:
                    front_prime()
                    left()
                    front()
                    left_prime()
                    break
                # put up to right
                if char_cube[5][2][1] == char_cube[2][1][1]:
                    front()
                    right_prime()
                    front_prime()
                    right()
                    break
            up()

        # if there is misplaced on right, from left side
        if not(char_cube[1][1][2] == 'y') and not(char_cube[2][1][0] == 'y') and (not(char_cube[1][1][2] == char_cube[1][1][1]) or not(char_cube[2][1][0] == char_cube[2][1][1])) and (char_cube[1][0][1] == 'y' or char_cube[5][2][1] == 'y'):
            front()                
            right_prime()
            front_prime()
            right()

        rotate_cw()
    # solve_stage = 4
    return solve_stage


    # if cube[0]
    # for s in range(0,4):
    #     if cube

def solve_white_corners(solve_stage):
    print('stage 4: solve white corners')
    bottom_layer_solved = True
    # check if bottom side is solved
    for s in range(0,4):
        for i in range(0,3):
            if not(char_cube[s][2][i] == char_cube[s][2][1]):
                bottom_layer_solved = False
                break
    # check if bottom white side is solved
    for i in range(0,3):
        for j in range(0,3):
            if not(char_cube[4][i][j] == 'w'):
                bottom_layer_solved = False

    if bottom_layer_solved == True:
        solve_stage = 5
        return solve_stage

    # corner placement algorithm

    # right side is white
    for s in range(0,4):
        for i in range(0,4):
            # right side is white
            if char_cube[2][0][0] == 'w':
                # if correct corner
                if char_cube[1][0][2] == char_cube[1][1][1] and char_cube[5][2][2] == char_cube[2][1][1]:
                    up()
                    front_prime()
                    up()
                    front()
                    up()
                    up()
                    front_prime()
                    up()
                    front()
                    break
            #front side is white
            if char_cube[1][0][2] == 'w':
                if char_cube[5][2][2] == char_cube[1][1][1] and char_cube[2][0][0] == char_cube[2][1][1]:
                    up_prime()
                    right()
                    up_prime()
                    right_prime()
                    up()
                    up()
                    right()
                    up_prime()
                    right_prime()
                    break
            # up side is white
            if char_cube[5][2][2] == 'w':
                if char_cube[2][0][0] == char_cube[1][1][1] and char_cube[1][0][2] == char_cube[2][1][1]:
                    for loop in range(0,3):
                        right()
                        up()
                        right_prime()
                        up_prime()
                    break
            up_prime()
        rotate_cw()
        # check if white corner on bottom
    for s in range(0,4):
        if (char_cube[4][0][2] == 'w' and not(char_cube[1][2][2] == char_cube[1][1][1]) and not(char_cube[2][2][0] == char_cube[2][1][1])) or char_cube[1][2][2] == 'w' or char_cube[2][2][0] =='w':
            for loop in range(0,3):
                right()
                up()
                right_prime()
                up_prime()
        rotate_cw()
        
     
    return solve_stage

def solve_yellow_cross(solve_stage):
    print('stage 5: solve yellow cross')
    yellow_cross = True

    if not(char_cube[5][0][1] == 'y' and char_cube[5][1][0] == 'y' and char_cube[5][1][2] == 'y' and char_cube[5][2][1] == 'y'):
        yellow_cross = False

    if yellow_cross == True:
        solve_stage = 6
        return solve_stage


    for s in range(0,4):
        # button
        # button = True
        # for i in range(0,3):
        #     if char_cube[5][0][i] == 'y' or char_cube[5][2][i] == 'y':
        #         button = False
        # if char_cube[5][1][0] == 'y' or char_cube[5][1][2] == 'y':
        #     button = False
        

        
        # if hook, do algorithm once after loop
        if char_cube[5][1][0] == 'y' and char_cube[5][0][1] == 'y':
            break
        # if bar, do it once now, then again after loop
        if char_cube[5][1][0] == 'y' and char_cube[5][1][2] == 'y':
            front()
            up()
            right()
            up_prime()
            right_prime()
            front_prime()
            break
        
        #otherwise, keep rotating until we find pattern above
        up()

    # runs if hook is found, if bar is found. if nothing found, run algorithm to get hook or bar next time
    front()
    up()
    right()
    up_prime()
    right_prime()
    front_prime()

    return solve_stage

def solve_yellow_side(solve_stage):
    print('stage 6: solve yellow side')

    yellow_side_solved = True
    for i in range(0,3):
        for j in range(0,3):
            if not(char_cube[5][i][j] == 'y'):
                yellow_side_solved = False
                break

    if yellow_side_solved:
        solve_stage = 7
        return solve_stage 

    # fish, cross, t, tl/br corner
    for s in range(0,4):

        # double fish
        double_fish = True
        for i in range(0,2):
            for j in range(0,2):
                if not(char_cube[5][i][j] == 'y'):
                    double_fish = False
                    break
                if not(char_cube[5][2-i][2-j] == 'y'):
                    double_fish = False
                    break
        if not(char_cube[1][0][0] == char_cube[2][0][2]):
            double_fish = False

        if double_fish:
            print('found a double fish')
            break
        
        # didn't add notch, not needed?
        # T shape
        T = True
        for i in range(0,2):
            for j in range(0,3):
                if not(char_cube[5][i][j] == 'y'):
                    T = False
                    break
        if T and char_cube[1][0][0] == char_cube[1][0][2]:
            print('found a T1')
            break
        
        if T and char_cube[0][0][2] == char_cube[2][0][0]:
            print('found a T2')
            break

        # inverse T - if we find an inverse T, do U2 to make it a T
        T_inv = True
        for i in range(0,2):
            for j in range(0,3):
                if not(char_cube[5][i+1][j] == 'y'):
                    T_inv = False
                    break
        if T_inv and char_cube[3][0][0] == char_cube[3][0][2]:
            print('found a T_inv1')
            up()
            up()
            break
        
        if T_inv and char_cube[2][0][2] == char_cube[0][0][0]:
            print('found a T_inv2')
            up()
            up()
            break


        # cross

        if char_cube[5][0][1] == 'y' and char_cube[5][1][0] == 'y' and char_cube[5][1][2] == 'y' and char_cube[5][2][1] == 'y':
            if char_cube[0][0][2] == 'y' and char_cube[2][0][0] == 'y' and char_cube[3][0][0] == 'y' and char_cube[3][0][2] == 'y':
                print('found a cross')
                break

        # fish
        if char_cube[5][0][1] == 'y' and char_cube[5][1][0] == 'y' and char_cube[5][1][2] == 'y' and char_cube[5][2][0] == 'y' and char_cube[5][2][1] == 'y':
            print('found a fish')
            break

        print('didnt find anything, doing up to find next pattern. current s = ',s)
        up()
    
    right()
    up()
    right_prime()
    up()
    right()
    up()
    up()
    right_prime()
    return solve_stage

def solve_last_layer(solve_stage):
    print('stage 7: solve_last_layer')

    same_corners = True

    # rotate to check if corner matches
    for s in range(0,4):
        if not(char_cube[s][0][0] == char_cube[s][1][1] and char_cube[s][0][2] == char_cube[s][1][1]):
            same_corners = False
            break
    
    if same_corners:
        solve_stage = 8
        return solve_stage

    for s in range(0,4):
        # if we find a matching corner
        if char_cube[s][0][0] == char_cube[s][0][2]:
            # put same corners at the back
            for i in range(0,3-s):
                up_prime()
            # rotate until corner matches center
            while not(char_cube[3][0][0] == char_cube[3][1][1]):
                rotate_cw()
                up_prime()
            break
    
    right_prime()
    front()
    right_prime()
    back()
    back()
    right()
    front_prime()
    right_prime()
    back()
    back()
    right()
    right()

    # rotate so then it's correct
    for s in range(0,4):
        # if we find a matching corner
        if char_cube[s][0][0] == char_cube[s][0][2]:
            while not(char_cube[s][0][0] == char_cube[s][1][1]):
                rotate_cw()
                up_prime()
            break


    return solve_stage

def solve_last_layer_middle(solve_stage):
    print('stage 8: solve last layer - middle pieces')

    last_layer = True

    for s in range(0,4):
        for i in range(0,3):
            if not(char_cube[s][0][i] == char_cube[s][1][1]):
                last_layer = False
                break
    
    if last_layer:
        solve_stage = 9
        return solve_stage
    
    for s in range(0,4):
        if char_cube[s][0][0] == char_cube[s][0][1] and char_cube[s][0][2] == char_cube[s][0][1]:
            color = char_cube[s][0][1]
            while not(char_cube[s][1][1] == color):
                rotate_cw()
                up_prime()
            # rotate side to back
            while not(char_cube[3][1][1] == color):
                rotate_cw()
            break
        up()

    # now the filled side is at the back, OR there are no filled sides, just apply algorithm
    # checking for clockwise
    if (char_cube[0][0][1] == char_cube[2][1][1] and char_cube[1][0][1] == char_cube[0][1][1] and char_cube[2][0][1] == char_cube[1][1][1]):
        right()
        right()
        up()
        right()
        up()
        right_prime()
        up_prime()
        right_prime()
        up_prime()
        right_prime()
        up()
        right_prime()
    else:
        right()
        up_prime()
        right()
        up()
        right()
        up()
        right()
        up_prime()
        right_prime()
        up_prime()
        right()
        right()
    
    return solve_stage












def is_cube_solved():
    for s in range(0,6):
        for i in range(0,3):
            for j in range(0,3):
                if not(char_cube[s][i][j] == char_cube[s][1][1]):
                    print('cube not solved')
                    return False
                    break
    print('cube solved!')
    return True


# initial setup
graphics_cube = []

side(blue, 125, 200, 50)
side(red, 300, 200, 50)
side(green, 475, 200, 50)
side(orange, 650, 200, 50)
side(white, 300, 375, 50)
side(yellow, 300, 25, 50)

char_cube = [[['b','b','b'],['b','b','b'],['b','b','b']], 
            [['r','r','r'],['r','r','r'],['r','r','r']], 
            [['g','g','g'],['g','g','g'],['g','g','g']], 
            [['o','o','o'],['o','o','o'],['o','o','o']],
            [['w','w','w'],['w','w','w'],['w','w','w']],
            [['y','y','y'],['y','y','y'],['y','y','y']]]

solving = False
cube_solved = is_cube_solved()
button_pressed = False

# buttons
start_button = button(surface, gray, 800, 100, 150, 75, 'start', white, 30)

up_button = button(surface, gray, 650, 400, 30, 30, 'U', white, 20)
up_prime_button = button(surface, gray, 700, 400, 30, 30, 'U\'', white, 20)
front_button = button(surface, gray, 650, 450, 30, 30, 'F', white, 20)
front_prime_button = button(surface, gray, 700, 450, 30, 30, 'F\'', white, 20)
down_button = button(surface, gray, 650, 500, 30, 30, 'D', white, 20)
down_prime_button = button(surface, gray, 700, 500, 30, 30, 'D\'', white, 20)

left_button = button(surface, gray, 550, 450, 30, 30, 'L', white, 20)
left_prime_button = button(surface, gray, 600, 450, 30, 30, 'L\'', white, 20)
right_button = button(surface, gray, 750, 450, 30, 30, 'R', white, 20)
right_prime_button = button(surface, gray, 800, 450, 30, 30, 'R\'', white, 20)
back_button = button(surface, gray, 850, 450, 30, 30, 'B', white, 20)
back_prime_button = button(surface, gray, 900, 450, 30, 30, 'B\'', white, 20)

rotate_cw_button = button(surface, gray, 825, 300, 100, 30, 'Rotate CW', white, 20)
scramble_button = button(surface, gray, 825, 350, 100, 30, 'Scramble', white, 20)
test_button = button(surface, gray, 825, 200, 75, 30, 'Test', white, 20)



# event loop
while True:
    # events in for loop
    for event in pygame.event.get():

        # check if user has quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # check if mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            mouse = rectangle(surface, black, mouse_x, mouse_y, 1, 1)

            # checks if a square is clicked
            for s in range(0,6):
                for i in range(0,3):
                    for j in range(0,3):
                        if mouse.intersects(graphics_cube[s][i][j]):
                            graphics_cube[s][i][j].color_increment()
                            break

            # checks for buttons
            if mouse.intersects(start_button):
                solving = True
            elif mouse.intersects(rotate_cw_button):
                if not(solving):
                    rotate_cw()
                # change solving after testing 
                button_pressed = True
            elif mouse.intersects(scramble_button):
                if not(solving):
                    scramble()
                # change solving after testing 
                button_pressed = True
            elif mouse.intersects(test_button):
                if not(solving):
                    test()
                # change solving after testing 
                button_pressed = True
            elif mouse.intersects(up_button):
                if not(solving):
                    up()
                # change solving after testing 
                button_pressed = True
            elif mouse.intersects(up_prime_button):
                if not(solving):
                    up_prime()
                # change solving after testing 
                button_pressed = True

            elif mouse.intersects(front_button):
                if not(solving):
                    front()
                # change solving after testing 
                button_pressed = True
            elif mouse.intersects(front_prime_button):
                if not(solving):
                    front_prime()
                # change solving after testing 
                button_pressed = True

            elif mouse.intersects(down_button):
                if not(solving):
                    down()
                # change solving after testing 
                button_pressed = True
            elif mouse.intersects(down_prime_button):
                if not(solving):
                    down_prime()
                # change solving after testing 
                button_pressed = True

            elif mouse.intersects(left_button):
                if not(solving):
                    left()
                # change solving after testing 
                button_pressed = True
            elif mouse.intersects(left_prime_button):
                if not(solving):
                    left_prime()
                # change solving after testing 
                button_pressed = True

            elif mouse.intersects(right_button):
                if not(solving):
                    right()
                # change solving after testing 
                button_pressed = True
            elif mouse.intersects(right_prime_button):
                if not(solving):
                    right_prime()   
                # change solving after testing 
                button_pressed = True

            elif mouse.intersects(back_button):
                if not(solving):
                    back()
                # change solving after testing 
                button_pressed = True
            elif mouse.intersects(back_prime_button):
                if not(solving):
                    back_prime()
                # change solving after testing 
                button_pressed = True




    # update content
    draw()
    if solving:
        solve()   
        solving = False

    else:
        graphics_to_cube(char_cube, graphics_cube)    

