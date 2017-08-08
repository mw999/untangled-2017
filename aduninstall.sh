#!/bin/bash
clear
echo "About to uninstall... Hold on!"
git checkout master
git pull
clear
echo "Sad to see you go."
echo "Just run the following to come back:"
echo "git checkout Admin & git pull & sh adinstall.sh"