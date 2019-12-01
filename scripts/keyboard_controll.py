#!/usr/bin/python3
import subprocess


def switch_us_cz_layouts():
    """
    Switches the keyboard layout between us and cz qwerty
    :return:
    """
    current_layout = get_current_layout()

    if current_layout == "us":
        subprocess.run("notify-send -t 900 'Setting the keyboard to czech'", shell=True)
        subprocess.run(["setxkbmap", "cz", "qwerty"])

    elif current_layout == "cz":
        subprocess.run("notify-send -t 900 'Setting the keyboard to english'", shell=True)
        subprocess.run(["setxkbmap", "us"])


def get_current_layout():
    """
    :return: A string with the current keyboard language code. (us, cz)
    """
    current_layout = subprocess.check_output("setxkbmap -query | grep layout | tail -c 3", shell=True).decode().rstrip()
    print(current_layout)
    return current_layout


if __name__ == '__main__':
    switch_us_cz_layouts()
