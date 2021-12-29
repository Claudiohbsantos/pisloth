from pisloth import Sloth
from robot_hat import Ultrasonic
from robot_hat import Pin
from robot_hat import TTS, Music

import time

# Sloth class instantiated with pin list. This is passed to 
# inherited Robot class. Lists with PWM pins are being used by servos 
sloth = Sloth([1,2,3,4])
# offsets to servo angles 
sloth.set_offset([-15,10,0,0])

# Initialize ultrasonic module
sonar = Ultrasonic(Pin("D2") ,Pin("D3"))
music = Music()

# excited reaction
sloth.add_action("eager", [
    [0, -40, 0, 40],
    [0, 0, 0, 0]
    ])

# Threshold for "closeness". unit: cm
close_distance = 6 
# Duration of search period in seconds
search_time = 10

last_seen = 0
curr_turn_step = 0
curr_turn_direction = "left"

def main():
    global last_seen
    global curr_turn_step
    global curr_turn_direction
    distance = sonar.read()

    # When waved at, act surprised and initiate next "search" phase
    if distance > 0 and distance <= close_distance:
        last_seen = time.time()
        curr_turn_step = 0
        curr_turn_direction = "left" if curr_turn_direction == "right" else "right"
        music.sound_effect_threading('../examples/sounds/sign.wav')
        sloth.do_action('eager', 1, 80)
    # If within "search" phase, turn around looking for object
    elif time.time() - last_seen <= search_time:
        sloth.servo_move(sloth.move_list["turn " + curr_turn_direction][curr_turn_step],90)

        # Execute turn steps one at a time to allow waves to interrupt turn action
        curr_turn_step += 1
        if curr_turn_step >= len(sloth.move_list["turn " + curr_turn_direction]):
            curr_turn_step = 0

if __name__ == "__main__":
    # do action forever
    while True:
        main()