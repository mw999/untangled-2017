#!/bin/bash
clear
echo "You're all set! Welcome to ADMIN 1.0.0!"
echo "Now for your name. What is it?"
read name
echo [Player] > player_save
echo name = [ADMIN] $name >> player_save
echo mute = false >> player_save
echo "Here we go, $name!"
sh start.sh
