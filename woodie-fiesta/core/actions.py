from keyboard import press_and_release
from pyautogui import center, moveTo, click, locateOnScreen
from time import sleep
from core.config import *

# move mouse to center of the tree
def move(location):
  x,y = center(location)
  moveTo(x, y)

# use axe on tree -> gather sticks, dried sticks, etc
def get_tree(location):
  if location != None:
    sleep(0.5)
    moveTo(REGION_AXE)
    click(REGION_AXE, button='right')
    sleep(0.5)
    move(location)
    click(button='left')
    sleep(1)

# click on minimap
def move_and_click(location):
  move(location)
  click()

# conjure rune (cast spell saved on F3 hotkey)
def conjure_rune():
  mana = locateOnScreen(MANA_IMG, confidence=0.6, region=REGION_MANA)
  if mana != None:
    press_and_release('F3')

# eat food (right slot of the small axe)
def eat_food():
  moveTo(REGION_FOOD)
  click(REGION_FOOD, button='right')
