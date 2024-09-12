# Human-Like Typing Simulation

This project simulates human typing using Python. The script reads content from a text file and types it in any active application. It mimics human typing speed by introducing random delays between keystrokes, simulating typing errors, and correcting them, just like a real person.

## Features
- Simulates human typing with random delays between keystrokes.
- Introduces typing errors and corrects them with backspace.
- Reads text content from a file (`text_to_type.txt`).
- Gives the user 5 seconds to switch to the desired application before typing starts.

## Requirements
- Python 3.x
- `pyautogui` library for keyboard simulation
- `random` and `time` libraries (part of the Python Standard Library)

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Hxrshrathore/human-like-typing-simulation.git
   cd human-like-typing-simulation
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv typing_env
   # Windows
   typing_env\Scripts\activate
   # macOS/Linux
   source typing_env/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install pyautogui keyboard
   ```

4. Create a text file named `text_to_type.txt` in the project directory and add the content you want the script to type:
   ```txt
   This is an example of text that will be typed by the script.
   ```

## Usage

1. Run the script:
   ```bash
   python human_typing.py
   ```

2. The script will give you 5 seconds to switch to the application where you want the text to be typed.

3. After 5 seconds, the script will simulate typing the text from `text_to_type.txt` in the active application, including random typing errors and corrections.

## Example

### Input (`text_to_type.txt`):
```txt
Hello, this is a test of human-like typing simulation.
```

### Output (typed in the target application):
```
Hello, thjis is a test of human-like typing simulation.
[backspace]is a test of human-like typing simulation.
```

## Notes

- The script does not actually make your machine recognized as an HID (Human Interface Device) by external systems. It simulates typing by controlling the keyboard through Python's `pyautogui` library.
- The typing speed is randomized to mimic the inconsistencies in human typing.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


### Key Sections Explained:
1. **Features**: Explains what the project does.
2. **Requirements**: Lists the necessary libraries.
3. **Installation**: Guides users on how to set up the project.
4. **Usage**: Shows how to run the project and what to expect.
5. **Example**: Demonstrates a simple input and output scenario.
6. **License**: States the license under which the project is shared.

