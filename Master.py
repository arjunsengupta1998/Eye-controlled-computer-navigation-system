#Master program to be run. Simply run this code on your linux terminal
#This program shall run both the following programs in background
#This will work for ubuntu only. For windows, check modification in commands
import os
import sys



os.system('python3 IrisCursor.py &')
os.system('python3 HackNew2.py --shape-predictor shape_predictor_68_face_landmarks.dat &')
