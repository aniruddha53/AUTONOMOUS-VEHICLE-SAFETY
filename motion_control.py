from __future__ import division
import time
import mycar_0_led

import Adafruit_PCA9685

mycar_0_led.setup() 
def replace_num(initial,new_num):   #Call this function to replace data in '.txt' file
    newline=""
    str_num=str(new_num)
    with open("set.txt","r") as f:
        for line in f.readlines():
            if(line.find(initial) == 0):
                line = initial+"%s" %(str_num+"\n")
            newline += line
    with open("set.txt","w") as f:
        f.writelines(newline)

def num_import_int(initial):        #Call this function to import data from '.txt' file
    with open("set.txt") as f:
        for line in f.readlines():
            if(line.find(initial) == 0):
                r=line
    begin=len(list(initial))
    snum=r[begin:]
    n=int(snum)
    return n

#import the settings for servos
vtr_mid_orig    = num_import_int('E_C1:')               #E_C1 : Middle of vertical motion
hoz_mid_orig    = num_import_int('E_C2:')               #E_C2 : Middle of horizontal motion

turn_right_max  = num_import_int('turn_right_max:')
turn_left_max   = num_import_int('turn_left_max:')
turn_middle     = num_import_int('turn_middle:')

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def turn_ang(ang):
    if ang < turn_right_max:
        ang = turn_right_max
    elif ang > turn_left_max:
        ang = turn_left_max
    else:
        pass
    pwm.set_pwm(2,0,ang)

def right():
    pwm.set_pwm(2, 0, turn_right_max)

def left():
    pwm.set_pwm(2, 0, turn_left_max)

def middle():
    pwm.set_pwm(2, 0, turn_middle)

def head_horizontal(hoz_mid):
    pwm.set_pwm(1, 0, hoz_mid)

def head_vertical(vtr_mid):
    pwm.set_pwm(0, 0, vtr_mid)

def ahead():
    pwm.set_pwm(1, 0, hoz_mid_orig)
    pwm.set_pwm(0, 0, vtr_mid_orig)


try:
    ahead()
    right()
    mycar_0_led.right_on()
    time.sleep(1)
    middle()
    mycar_0_led.both_off()
    time.sleep(1)
    left()
    mycar_0_led.left_on()
    time.sleep(1)
    middle()
    mycar_0_led.both_off()
    time.sleep(1)
    head_horizontal(90)
    time.sleep(1)
    ahead()
    time.sleep(1)
    head_horizontal(330)
    time.sleep(1)
    ahead()
    time.sleep(1)
    head_vertical(380) 
    time.sleep(1)
    ahead()
    time.sleep(1)
    head_vertical(70)
    time.sleep(1)
     
except KeyboardInterrupt:
    destroy()