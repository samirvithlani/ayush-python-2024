import pyscreenshot
from datetime import datetime
import time

# Function to take and save screenshot with current date and time
def take_screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Get current date and time
    print(timestamp)
    filename = f"screenshot_{timestamp}.png"  # Construct filename with timestamp
    print(filename)
    image = pyscreenshot.grab()  # Capture the screen
    image.save("pqr.png")  # Save the screenshot with the constructed filename
    print(f"Screenshot taken and saved as {filename}")

# Main loop to take screenshots at one-minute intervals
while True:
    take_screenshot()  # Take a screenshot
    time.sleep(60)  # Wait for one minute before taking the next screenshot
