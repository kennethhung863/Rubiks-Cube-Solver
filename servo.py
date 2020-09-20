import serial
import time
# connecting arduino port to python program
###########################
# change the port here!!
###########################
ser = serial.Serial('COM8', 115200, timeout=None)
time.sleep(2)

def rotate_1():
  ser.write(b'0')
  ser.read()
def rotate_2():
  ser.write(b'1')
  ser.read()
def rotate_3():
  ser.write(b'2')
  ser.read()
def push():
  ser.write(b'3')
  ser.read()
def hold():
  ser.write(b'4')
  ser.read()
def release():
  ser.write(b'5')
  ser.read()
def turn_2_to_3():
  ser.write(b'6')
  ser.read()
def turn_2_to_1():
  ser.write(b'7')
  ser.read()


def up():
  push()
  push()
  turn_2_to_3()
  rotate_2()
  push()
  rotate_3()
  push()
  rotate_2()
  push()

def up_prime():
  push()
  push()
  turn_2_to_1()
  rotate_2()
  push()
  rotate_1()
  push()
  rotate_2()
  push()

def down():
  turn_2_to_3()
  rotate_2()
  push()
  rotate_3()
  push()
  rotate_2()
  push()
  push()
  push()

def down_prime():
  turn_2_to_1()
  rotate_2()
  push()
  rotate_1()
  push()
  rotate_2()
  push()
  push()
  push()

def left():
  rotate_3()
  push()
  rotate_2()
  turn_2_to_3()
  rotate_1()
  push()
  rotate_2()
  push()

def left_prime():
  # rotate_3()
  # push()
  # hold()
  # rotate_2()
  # release()
  # rotate_1()
  # push()
  # rotate_2()
  # push()
  # push()
  # push()

  # push()
  # rotate_3()
  # push()
  # rotate_2()
  # turn_2_to_1()
  # # rotate_1()
  # push()
  # rotate_2()
  # push()
  # push()
  # # push()

  rotate_3()
  push()
  rotate_2()
  turn_2_to_1()
  push()
  rotate_2()
  push()
  push()
  push()

def right():
  # rotate_1()
  # push()
  # hold()
  # rotate_2()
  # release()
  # rotate_3()
  # push()
  # rotate_2()
  # push()
  # push()
  # push()

  rotate_1()
  push()
  rotate_2()
  turn_2_to_3()
  push()
  rotate_2()
  push()
  push()
  push()

def right_prime():
  rotate_1()
  push()
  rotate_2()
  turn_2_to_1()
  rotate_3()
  push()
  rotate_2()
  push()

def front():
  push()
  turn_2_to_3()
  rotate_2()
  push()
  push()
  push()
  rotate_1()
  push()
  rotate_2()

def front_prime():
  push()
  turn_2_to_1()
  rotate_2()
  push()
  push()
  push()
  rotate_3()
  push()
  rotate_2()

def back():
  push()
  push()
  push()
  turn_2_to_3()
  rotate_2()
  push()
  rotate_3()
  push()
  rotate_2()

def back_prime():
  push()
  push()
  push()
  turn_2_to_1()
  rotate_2()
  push()
  rotate_1()
  push()
  rotate_2()

def rotate_cw():
  push()
  rotate_1()
  push()
  rotate_2()
  push()
  push()
  push()