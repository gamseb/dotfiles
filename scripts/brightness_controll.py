#!/usr/bin/python3

import subprocess, argparse


def control_brightness(inc, dec):
    """
    The brightness of the computer screen is changed corresponding to the value of 'inc' and 'dec'.
    The values must be decimal numbers.
    :param inc: By how much to increase the brightness of the screen.
    :param dec: By how much to decrease the brightness of the screen.
    """
    if inc is None:
        inc = 0
    if dec is None:
        dec = 0

    delta = float(inc - dec)
    # current_brightness = subprocess.check_output("xrandr --verbose | grep -i brightness", shell=True)
    # brightness_number = float(current_brightness.decode()[-5:-1])
    current_brightness = get_current_brightness()
    target_brightness = current_brightness + delta

    print("Current brightness: {} \n Target brightness: {}".format(current_brightness, target_brightness))

    subprocess.run(["xrandr", "--output", "eDP-1", "--brightness", str(target_brightness)])
    subprocess.run("notify-send -t 450 'The brightness has been changed to: {}'".format(str(target_brightness)[:4]),
                   shell=True)


def set_brightness(value):
    """
    Sets the brightness of the screen
    :param value: brightness setting
    """
    if 0 > value > 1.5:
        print("The brightness value is set too hight or too low: ({})".format(str(value)))
        return
    subprocess.run(["xrandr", "--output", "eDP-1", "--brightness", str(value)])
    subprocess.run("notify-send -t 450 'The brightness has been changed to: {}'".format(str(value)[:4]), shell=True)


def activate_night_mode():
    """
    Night light (limiting blue light)
        Magenta: 1.1:0.8:0.7
        Lighter reddish colour 1.1:0.9:0.9
    """
    current_brightness = get_current_brightness()

    subprocess.run(["xrandr", "--output", "eDP-1", "--gamma", "1.1:0.9:0.9", "--brightness", str(current_brightness)])
    subprocess.run("notify-send -t 450 'Night mode has been activated'", shell=True)


def activate_day_mode():
    current_brightness = get_current_brightness()

    subprocess.run(["xrandr", "--output", "eDP-1", "--gamma", "1:1:1", "--brightness", str(current_brightness)])
    subprocess.run("notify-send -t 450 'Day mode has been activated'", shell=True)


def get_current_brightness():
    """
    Returns the current screen brightness.
    :return: The current brightness as a decimal number (float).
    """
    current_brightness_tmp = subprocess.check_output("xrandr --verbose | grep -i brightness", shell=True)
    current_brightness = float(current_brightness_tmp.decode()[-5:-1])
    return current_brightness


def parse_arguments():
    """
    Parses the arguments to know by how much to change the brightness
    :return: Returns the increase and decrease amount variables as integers
    """
    parser = argparse.ArgumentParser(description='Increase or decrease the brightness of the screen.')
    parser.add_argument("-inc", help="Increases the brightness", type=float)
    parser.add_argument("-dec", help="Decreases the brightness", type=float)
    parser.add_argument("-set", help="Set the brightness", type=float)
    parser.add_argument("-night", help="Set night mode", action='store_true')
    parser.add_argument("-day", help="Set day mode", action='store_true')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    arguments = parse_arguments()
    inc_value = vars(arguments)["inc"]
    dec_value = vars(arguments)["dec"]
    set_value = vars(arguments)["set"]
    night_light = vars(arguments)["night"]
    day_light = vars(arguments)["day"]

    if day_light is True:
        activate_day_mode()

    if night_light is True:
        activate_night_mode()

    if set_value is not None:
        set_brightness(set_value)

    if dec_value is not None or inc_value is not None:
        control_brightness(inc_value, dec_value)
