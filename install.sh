#!/usr/bin/env sh

######################################################################
# @author      : ekoehler (ekoehler@$HOSTNAME)
# @file        : install
# @created     : mardi nov. 09, 2021 15:10:10 CET
#
# @description : installs libs if not already installed
######################################################################

pip3 install python-espeak ffmpeg-python pyttsx3 speechRecognition pywhatkit wikipedia

echo "If this does't work, you may have to install espeak using your package manager"
