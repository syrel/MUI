from jha.shortcutter import *

# Simulate ALT + R
def ToggleRecording():
    PressKey(VK_MENU)  # Alt
    PressKey(VK_R)
    ReleaseKey(VK_R)
    time.sleep(1)
    ReleaseKey(VK_MENU)

if __name__ == "__main__":
    ToggleRecording()