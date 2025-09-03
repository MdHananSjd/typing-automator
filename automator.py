import pyautogui as pg
import time

print("Typing will start in 5 seconds...")
time.sleep(5)

text_to_write = '''
Enter the test you wanna type here
'''

pg.write(text_to_write, interval=0.03)