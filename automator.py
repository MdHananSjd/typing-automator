import pyautogui as pg
import time

print("Typing will start in 3 seconds...")
time.sleep(3)

text_to_write = '''
Enter the test you wanna type here
'''

pg.write(text_to_write, interval=0.03)