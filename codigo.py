import pyautogui as gui

gui.PAUSE = 2

gui.press("win")

gui.write("chrome")

gui.press("enter")

gui.write("youtube.com")

gui.press("enter")

#for i in range(4):
#   gui.press("tab")

x = 590
y = 110

gui.click(x, y)

gui.press("enter")

gui.write("gremio campeao do mundo")

gui.press("enter")

x = 420 
y = 270

gui.click(x, y)

x = 590
y = 710

gui.click(x, y)

