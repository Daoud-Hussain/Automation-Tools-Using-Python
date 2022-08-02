import pyautogui as pg
import time

print("This is working")
time.sleep(5)

for i in range(100):
   pg.write("Hey! I am auto-generated")
   time.sleep(0.5)
   pg.press("Enter")
    
    