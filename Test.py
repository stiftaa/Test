import ctypes
import time
    
    # Maus-Event-Konstanten
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
    
def click():
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
def autoklicker(interval):
    try:
        while True:
            click()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Autoklicker gestoppt.")
    
if __name__ == "__main__":
    clicks_per_second = float(input("Geben Sie die Anzahl der Klicks pro Sekunde ein: "))
    interval = 1.0 / clicks_per_second
    print("Drücken Sie Strg+C, um den Autoklicker zu stoppen.")
    autoklicker(interval)