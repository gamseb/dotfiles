#!/usr/bin/bash
CURRENT_KEYBOARD="$(setxkbmap -query | grep layout | tail -c 3)"
echo "$CURRENT_KEYBOARD"
if [ $CURRENT_KEYBOARD == "cz" ]; then
  notify-send "Setting the keyboard to english"
  setxkbmap us
elif [ $CURRENT_KEYBOARD == "us" ]; then 
  notify-send "Setting the keyboard to czech"
  setxkbmap cz qwerty
fi
