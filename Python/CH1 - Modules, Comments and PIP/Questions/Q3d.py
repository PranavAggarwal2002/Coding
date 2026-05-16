import os
import pyttsx3

engine = pyttsx3.init()

# Get current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create full file path
file_path = os.path.join(current_dir, "test1.mp3")

engine.say("Hello World!")
engine.save_to_file("Hello World", file_path)
engine.runAndWait()

print("Saved at:", file_path)