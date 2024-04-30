import subprocess
import time

def suma(x1, x2):
    return x1 + x2

def openCalc():
    subprocess.Popen("calc.exe")

def openw():
    subprocess.Popen("mspaint.exe")

def openp():
    subprocess.Popen("powerpnt.exe")
