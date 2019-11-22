#!/usr/bin/python3

import subprocess, argparse


def control_brightness(inc, dec):
    # assert inc, dec is float or None
    # inc = 0 if None else inc
    # dec = 0 if None else dec
    if inc is None:
        inc = 0
    if dec is None:
        dec = 0

    delta = float(inc - dec)
    current_brightness = subprocess.check_output("xrandr --verbose | grep -i brightness", shell=True)
    brightness_number = float(current_brightness.decode()[-5:-1])
    target_brightness = brightness_number + delta

    print("Current brightness: {} \n Target brightness: {}".format(brightness_number, target_brightness))

    subprocess.run(["xrandr", "--output", "eDP-1", "--brightness", str(target_brightness)])
    subprocess.run("notify-send 'The brightness has been changed to: {}'".format(str(target_brightness)[:4]), shell=True)



def parse_arguments():
    """
    Parses the arguments to know by how much to change the brightness
    :return: Returns the increase and decrease amount variables as integers
    """
    parser = argparse.ArgumentParser(description='Increase or decrease the brightness of the screen.')
    parser.add_argument("-inc", help="Increases the brightness", type=float)
    parser.add_argument("-dec", help="Decreases the brightness", type=float)

    args = parser.parse_args()
    inc = vars(args)["inc"]
    dec = vars(args)["dec"]

    return inc, dec


if __name__ == '__main__':
    inc, dec = parse_arguments()
    print("Inc:{} n\ Dec:{}".format(inc, dec))
    control_brightness(inc, dec)
    # print()
