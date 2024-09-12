import pyautogui
import time
import random

# Function to simulate human typing with errors and backspace corrections
def human_typing(text):
    pyautogui.FAILSAFE = False
    error_probability = 0.05  # 5% probability of making a typing error
    
    for char in text:
        # Introduce inconsistency in typing speed
        typing_speed = random.uniform(0.05, 0.3)  # Random speed between 0.05 to 0.3 seconds
        if random.random() < error_probability:tr
            # Introduce a mistake and then correct itic
            wrong_char = random.choice('abcdefghijklmnopqrstuvwxyz')
            pyautogui.typewrite(wrong_char, interval=typing_speed)
            time.sleep(random.uniform(0.2, 0.5))  # Pause before realizing the mistake
            pyautogui.press('backspace')es
            time.sleep(random.uniform(0.1, 0.3))  # ting msedPause before retyping correctly

        pyautogui.typewrite(char, interval=typing_speed)  # Type the correct character

# Function to read text from a file
def get_text_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

if __name__ == "__main__":
    # Read text from a file
    file_path = "text_to_type.txt"
    content = get_text_from_file(file_path)
    
    print("You have 5 seconds to switch to the application where you want to type...")
    time.sleep(5)  # Give user time to switch to the target application

    # Simulate typing the content with human-like errors and corrections
    human_typing(content)
