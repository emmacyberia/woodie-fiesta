from pyautogui import screenshot
from pynput.mouse import Listener

# Usage:
  # Mouse left click: take a picture of the mouse position on minmap (20x20 pixels)
  # Mouse right click: stop this program

class Photo:
  def __init__(self):
    self.count = 0

  def take_photo(self, x, y):
    my_screen = screenshot(region=(x - 10, y -10, 20, 20))
    path = 'icons/icon_{}.png'.format(self.count)
    self.count = self.count + 1
    my_screen.save(path)
  
  def click(self, x, y, button, pressed):
    if button.name == 'right':
      return False
    if pressed:
      self.take_photo(x, y)

photo = Photo()

with Listener(on_click=photo.click) as listener:
  listener.join()
