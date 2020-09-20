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
from rubik_solver import utils

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
    cube_string = ""
    
    # convert cube to string
    for row in range(3):
        for col in range(3):
            cube_string += char_cube[5][row][col]
    for side in range(4):
        for row in range(3):
            for col in range(3):
                cube_string += char_cube[side][row][col]
    for row in range(3):
        for col in range(3):
            cube_string += char_cube[4][row][col]

    # solve cube
    if (not(is_cube_solved())):
        solve_steps = utils.solve(cube_string, 'Kociemba')
    else:
        solve_steps = []


    execute_steps(solve_steps)
    print(solve_steps)
    print(cube_string)
    print('finished solving')
    

def execute_steps(solve_steps):
    for step in range(len(solve_steps)):
        turn = solve_steps[step]
        if turn == 'U':
            up()
        elif turn == 'U2':
            up()
            up()
        elif turn == 'U\'':
            up_prime()
        elif turn == 'D':
            down()
        elif turn == 'D2':
            down()
            down()
        elif turn == 'D\'':
            down_prime()
        elif turn == 'L':
            left()
        elif turn == 'L2':
            left()
            left()
        elif turn == 'L\'':
            left_prime()
        elif turn == 'R':
            right()
        elif turn == 'R2':
            right()
            right()
        elif turn == 'R\'':
            right_prime()
        elif turn == 'F':
            front()
        elif turn == 'F2':
            front()
            front()
        elif turn == 'F\'':
            front_prime()
        elif turn == 'B':
            back()
        elif turn == 'B2':
            back()
            back()
        elif turn == 'B\'':
            back_prime()

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

