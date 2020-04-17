# Rubiks Cube Solver by Kenneth Hung

*currently refining GUI and console text display*

#### This is a Python program which can solve a Rubik's cube using a layer-by-layer approach. The cube is represented as a 2D cube net with the GUI programmed using PyGame, which is updated in real-time as the cube is being solved. The program has buttons for turns, scramble, testing and solve.

To start, download all files and run "rubiks_solver.py". From there, the GUI should appear.

### Cube Display
By default, the cube will look like such, where the letters represent the colors on a cube

                            ['y', 'y', 'y']
                            ['y', 'y', 'y']
                            ['y', 'y', 'y']
                      
      ['b', 'b', 'b']       ['r', 'r', 'r']       ['g', 'g', 'g']       ['o', 'o', 'o']
      ['b', 'b', 'b']       ['r', 'r', 'r']       ['g', 'g', 'g']       ['o', 'o', 'o']
      ['b', 'b', 'b']       ['r', 'r', 'r']       ['g', 'g', 'g']       ['o', 'o', 'o']

                            ['w', 'w', 'w']
                            ['w', 'w', 'w']
                            ['w', 'w', 'w']


### Notations
The sides are represented as:
Front = Red

Left = Blue

Right = Green

Back = Orange

Up = Yellow

Down = White


Rotations are in quarter turns, where a normal rotation is CLOCKWISE, and the opposite is COUNTERCLOCKWISE.
ie. F = Front CW, F' = Front CCW

NOTE: These sides are the default starting notations. In the program, the algorithm can rotate the entire cube clockwise, denoted as
"Rotate CW". This shifts all the sides that aren't up or down to the left once graphically, and a new front is assigned. The colors above
are NOT constantly in the same position, except white and yellow.


### Features

Color Inputs
 - Press a square on the cube and the color will change. This is the primary method of inputting a scrambled cube for solving

Turn and Rotate Buttons
 - Multiple buttons in the same format as the cube net positions are available for use. Press a turn button and the turn will execute accordingly
 - The "Rotate CW" button rotates the entire cube clockwise. See more in the note under "Cube Display"
 
Scramble Button
 - Randomly shuffles the cube with multiple turns
 
Test Button (FOR DEVELOPMENT)
 - Used during development. Pressing the button will cause the program to solve a shuffled cube, then repeat
 
 Solve Button
  - When there is a scrambled cube, press to solve! Steps and stages will appear in the console terminal
  
 ### How It Works
 When the solve button is pressed, the on screen graphical cube is converted into a char array, where the set algorithm then begins to execute. It uses a basic layer-by-layer approach which is what I personally use to solve the cube. Once a stage is complete, it will move on to the next. At the final stage, the cube is solved. Below is a brief summary of the solving stages.
 
 1. Solve white cross without aligned bottom layer
 2. Solve white cross with aligned bottom layer
 3. Solve middle layer
 4. Solve white corner
 5. Solve yellow cross
 6. Solve yellow side without aligned top layer
 7. Permute last layer part 1
 8. Permute last layer part 2
 
 ### Notes
  - If the program terminates while solving and you inputted colors for the solve, the colors on the cube aren't inputted correctly. Misaligned sides, even if there is enough colors on the cube, are unsolvable. Try to input the colors again.
  - The program will show all turns from the initial stage to solved stage, but it will most likely not be optimal. The approach is not meant to be a speed solving one, and is for use with a Raspberry Pi to solve a real cube using servos for a personal project in development.
