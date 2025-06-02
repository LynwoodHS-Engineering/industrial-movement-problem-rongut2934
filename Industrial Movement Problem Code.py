#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
motor_group_1_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_group_1_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
motor_group_1 = MotorGroup(motor_group_1_motor_a, motor_group_1_motor_b)
motor_group_3_motor_a = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
motor_group_3_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
motor_group_3 = MotorGroup(motor_group_3_motor_a, motor_group_3_motor_b)
motor393_a = Motor29(brain.three_wire_port.a, False)
motor393_b = Motor29(brain.three_wire_port.b, False)
motor393_c = Motor29(brain.three_wire_port.c, False)
motor393_d = Motor29(brain.three_wire_port.d, False)
motor393_e = Motor29(brain.three_wire_port.e, False)
motor393_f = Motor29(brain.three_wire_port.f, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code

# Authors: Ronald Gutierrez & Diego Esquivel

# Project: Final Semester Project - Industrial Product Movement



motor_group_1_motor_a.spin(FORWARD)  # system to desired direction towards the dropoff box
motor_group_1_motor_b.spin(FORWARD)
motor_group_3_motor_a.spin(REVERSE)
motor_group_3_motor_b.spin(REVERSE)

wait(4,SECONDS)

motor_group_1_motor_a.stop()
motor_group_1_motor_b.stop()
motor_group_3_motor_a.stop()
motor_group_3_motor_b.stop()

wait(2,SECONDS)

motor_group_1_motor_a.spin(REVERSE)  # system to desired direction towards the dropoff box
motor_group_1_motor_b.spin(REVERSE)
motor_group_3_motor_a.spin(FORWARD)
motor_group_3_motor_b.spin(FORWARD)

wait(4,SECONDS)

motor_group_1_motor_a.stop()
motor_group_1_motor_b.stop()
motor_group_3_motor_a.stop()
motor_group_3_motor_b.stop()

wait(2,SECONDS)

motor393_e.spin(FORWARD)  # scoop will pick up alleged ball
motor393_f.spin(REVERSE)

wait(5,SECONDS)  

motor_group_1_motor_a.spin(REVERSE)  # Drivetrain system will move to desired dropoff position
motor_group_1_motor_b.spin(REVERSE)
motor_group_3_motor_a.spin(FORWARD)
motor_group_3_motor_b.spin(FORWARD)

wait(8,SECONDS)

motor_group_1_motor_a.stop() # temporary stop
motor_group_1_motor_b.stop()
motor_group_3_motor_a.stop()
motor_group_3_motor_b.stop()

wait(2,SECONDS)

motor_group_1_motor_a.set_velocity(10,PERCENT)  # system is slowed to ensure efficiency
motor_group_1_motor_b.set_velocity(10,PERCENT)
motor_group_3_motor_a.set_velocity(10,PERCENT)
motor_group_3_motor_b.set_velocity(10,PERCENT)

motor_group_1_motor_a.spin(REVERSE)  # system spins to desired direction towards the dropoff box
motor_group_1_motor_b.spin(FORWARD)
motor_group_3_motor_a.spin(REVERSE)
motor_group_3_motor_b.spin(FORWARD)

wait(5.75,SECONDS)

motor_group_1_motor_a.stop()  
motor_group_1_motor_b.stop()
motor_group_3_motor_a.stop()
motor_group_3_motor_b.stop()

wait(2,SECONDS)

motor_group_1_motor_a.spin(FORWARD)  # system to desired direction towards the dropoff box
motor_group_1_motor_b.spin(FORWARD)
motor_group_3_motor_a.spin(REVERSE)
motor_group_3_motor_b.spin(REVERSE)

wait(5,SECONDS)

motor_group_1_motor_a.stop()  
motor_group_1_motor_b.stop()
motor_group_3_motor_a.stop()
motor_group_3_motor_b.stop()

wait(2,SECONDS)

motor393_a.spin(REVERSE)  #Chain Lift will raise the ball to desired level
motor393_b.spin(REVERSE)
motor393_c.spin(FORWARD)
motor393_d.spin(FORWARD)

wait(7,SECONDS)

motor393_a.stop()  # Temporary stop to set position
motor393_b.stop()
motor393_c.stop()
motor393_d.stop()

wait(2,SECONDS)

motor393_e.stop()
motor393_f.stop()

wait(2,SECONDS)

motor393_a.spin(FORWARD)  #Chain lift will revert back to orignal position
motor393_b.spin(FORWARD)
motor393_c.spin(REVERSE)
motor393_d.spin(REVERSE)

wait(4,SECONDS)

motor393_a.stop() 
motor393_b.stop()
motor393_c.stop()
motor393_d.stop()

wait(2,SECONDS)

motor_group_1_motor_a.spin(REVERSE)     # Sytstem will revert back to orignal position
motor_group_1_motor_b.spin(REVERSE)
motor_group_3_motor_a.spin(FORWARD)
motor_group_3_motor_b.spin(FORWARD)

wait(14,SECONDS)

motor_group_1_motor_a.stop()
motor_group_1_motor_b.stop()
motor_group_3_motor_a.stop()
motor_group_3_motor_b.stop()

wait(2,SECONDS)

motor_group_1_motor_a.set_velocity(10,PERCENT)  # System is slowed to ensure efficiency
motor_group_1_motor_b.set_velocity(10,PERCENT)
motor_group_3_motor_a.set_velocity(10,PERCENT)
motor_group_3_motor_b.set_velocity(10,PERCENT)

motor_group_1_motor_a.spin(REVERSE)  # system spins to desired direction towards the pick up box
motor_group_1_motor_b.spin(FORWARD)
motor_group_3_motor_a.spin(REVERSE)
motor_group_3_motor_b.spin(FORWARD)

wait(5,SECONDS)

motor_group_1_motor_a.stop()  # system spins to desired direction towards the pickup box
motor_group_1_motor_b.stop()
motor_group_3_motor_a.stop()
motor_group_3_motor_b.stop()

wait(2,SECONDS)

