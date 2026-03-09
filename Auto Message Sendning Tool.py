import pyautogui 
import time
message = 100I miss you so much.

while message > 0: # This will run the loop until the message variable is greater than 0.
    time.sleep(1) # This will wait for 1 second before pressing the keys again.
    pyautogui.typewrite("I miss you so much.") # This will type the text "I miss you so much." repeatedly until the program is stopped.
    time.sleep(1) # This will wait for 1 second before pressing the keys again.
    pyautogui.press("enter") # This will press the enter key to submit the message.
    message = message - 1 # This will decrease the value of the message variable by 1 after each iteration of the loop.
I miss you so much.
I miss you so much.
I miss you so much.
I miss you so much.
I miss you so much.
I miss you so much.
I miss you so much.
