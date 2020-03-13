import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as kController
import curses
import os
import threading
import sys
from random import randint
from multiprocessing import Queue

shouldRun = False
mouse = Controller()
keyboard = kController()


def worker():
	global shouldRun
	while True:
		while(shouldRun == True):
			keyboard.press(Key.f15)
			keyboard.release(Key.f15)
			mouse.move(1, -1)
			mouse.move(-1, 1)
			# wait a random time between 25 and 50 seconds before sending the next key press/mouse movement
			time.sleep(randint(25,50))

def main(win):

	global shouldRun

	listen = threading.Thread(target=worker)
	listen.daemon = True
	listen.start()

	win.nodelay(False)
	key=""
	win.clear()
	win.addstr("Worker is inactive\nPress Enter to activate: ")
	win.addstr("\n\n\n")
	win.addstr    ("\n")
	win.addstr    ("\n")
	win.addstr    ("\n                                  ####  ####")
	win.addstr    ("\n")
	win.addstr    ("\n                                      ##")
	win.addstr    ("\n                                      ##")
	win.addstr    ("\n")
	win.addstr    ("\n")
	win.addstr    ("\n                                  ##########")
	while True:
		try:
			key = win.getch()
			win.clear()

			#win.addstr("Detected key:")



			if key == 3:
				sys.exit()
			if key == 10 or key == 529:
				if shouldRun == False:
					shouldRun = True
				else:
					shouldRun = False
			if key == os.linesep:
				break

			if shouldRun == True:
				win.clear()
				win.addstr("Worker is active!\nPress Enter to deactivate: ")
				win.addstr("\n\n\n                                   ##    ##")
				win.addstr    ("\n                                   ##    ##")
				win.addstr    ("\n                                   ##    ##")
				win.addstr    ("\n                                   ##    ##")
				win.addstr    ("\n")
				win.addstr    ("\n                                      ##")
				win.addstr    ("\n                                      ##")
				win.addstr    ("\n")
				win.addstr    ("\n                                  ##      ##")
				win.addstr    ("\n                                  ##########")
			else:
				win.addstr("Worker is inactive\nPress Enter to activate: ")
				win.addstr("\n\n\n")
				win.addstr    ("\n")
				win.addstr    ("\n")
				win.addstr    ("\n                                  ####  ####")
				win.addstr    ("\n")
				win.addstr    ("\n                                      ##")
				win.addstr    ("\n                                      ##")
				win.addstr    ("\n")
				win.addstr    ("\n")
				win.addstr    ("\n                                  ##########")
		except Exception as e:
			# No input
			#print(e)
			pass

curses.wrapper(main)
