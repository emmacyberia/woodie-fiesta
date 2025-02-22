from time import sleep
from keyboard import wait
from pyautogui import locateOnScreen
from core.config import *
from core.actions import move, get_tree, move_and_click, conjure_rune, eat_food

# press P in-game to start running
keyboard.wait('p')

tree_counter = 0

while True:
  for index in range(61):
    while True:
      position_in_map = pyautogui.locateOnScreen('assets/icons/icon_{}.png'.format(index), confidence=0.90, region=REGION_MINIMAP)
      print('waypoint: {}'.format(index))
      if position_in_map != None:
        move_and_click(position_in_map)
        sleep(6)
        conjure_rune()
        eat_food()
        sleep(0.5)
        print('Harvested trees: {}'.format(tree_counter))
        check_position = pyautogui.locateOnScreen('assets/icons/icon_{}.png'.format(index), confidence=0.90, region=REGION_MINIMAP)
        if check_position == None:
          tree_counter += 1
          for position in list_positions:
            for index in range(8):
              while True:
                tree = pyautogui.locateOnScreen('assets/trees/tree_{}.PNG'.format(index), confidence=0.7, region=position)
                if tree != None:
                  get_tree(tree)
                else:
                  break
          break
