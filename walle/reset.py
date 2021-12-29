from pisloth import Sloth

# Sloth class instantiated with pin list. This is passed to 
# inherited Robot class. Lists with PWM pins are being used by servos 
sloth = Sloth([1,2,3,4])
# offsets to servo angles 
sloth.set_offset([-15,10,0,0])

def main():
    sloth.do_action('stand')


if __name__ == "__main__":
    main()