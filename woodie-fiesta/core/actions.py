from keyboard import press_and_release, wait
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

# press P in-game to start running
keyboard.wait('p')

def main():
  while True:
    for index in range(61):
      while True:
        position_in_map = locateOnScreen('woodie-fiesta/assets/icons/icon_{}.png'.format(index), confidence=0.90, region=REGION_MINIMAP)
        print('waypoint: {}'.format(index))
        if position_in_map != None:
          move_and_click(position_in_map)
          sleep(6)
          conjure_rune()
          eat_food()
          sleep(0.5)
          print('Harvested trees: {}'.format(tree_counter))
          check_position = locateOnScreen('woodie-fiesta/assets/icons/icon_{}.png'.format(index), confidence=0.90, region=REGION_MINIMAP)
          if check_position == None:
            tree_counter += 1
            for position in list_positions:
              for index in range(8):
                while True:
                  tree = locateOnScreen('woodie-fiesta/assets/trees/tree_{}.PNG'.format(index), confidence=0.7, region=position)
                  if tree != None:
                    get_tree(tree)
                  else:
                    break
          break
