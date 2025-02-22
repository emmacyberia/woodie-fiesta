from keyboard import press_and_release
from pyautogui import center, moveTo, click, locateOnScreen
from time import sleep
from core.config import *

# move mouse to center of the tree
def move(location):
  x,y = pyautogui.center(location)
  pyautogui.moveTo(x, y)

# use axe on tree -> gather sticks, dried sticks, etc
def get_tree(location):
  if location != None:
    sleep(0.5)
    pyautogui.moveTo(REGION_AXE)
    pyautogui.click(REGION_AXE, button='right')
    sleep(0.5)
    move(location)
    pyautogui.click(button='left')
    sleep(1)

# click on minimap
def move_and_click(location):
  move(location)
  pyautogui.click()

# conjure rune (cast spell saved on F3 hotkey)
def conjure_rune():
  mana = pyautogui.locateOnScreen(MANA_IMG, confidence=0.6, region=REGION_MANA)
  if mana != None:
    keyboard.press_and_release('F3')

# eat food (right slot of the small axe)
def eat_food():
  pyautogui.moveTo(REGION_FOOD)
  pyautogui.click(REGION_FOOD, button='right')
