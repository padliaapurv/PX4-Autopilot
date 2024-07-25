# keyboard_control.py

from pymavlink import mavutil
from pynput import keyboard

class KeyboardControl:
    def __init__(self, connection_string):
        self.mav = mavutil.mavlink_connection(connection_string)
        self.mav.wait_heartbeat()
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def on_press(self, key):
        try:
            if key.char == 'w':
                self.send_control(1, 0, 0)  # Move forward
            elif key.char == 's':
                self.send_control(-1, 0, 0)  # Move backward
            elif key.char == 'a':
                self.send_control(0, -1, 0)  # Turn left
            elif key.char == 'd':
                self.send_control(0, 1, 0)  # Turn right
            elif key.char == ' ':
                self.send_control(0, 0, 1)  # Ascend
            elif key.char == 'x':
                self.send_control(0, 0, -1)  # Descend
        except AttributeError:
            pass

    def send_control(self, x, y, z):
        # Send MAVLink manual control message
        self.mav.mav.manual_control_send(
            0,  # Target system
            int(x * 1000),  # X axis control
            int(y * 1000),  # Y axis control
            int(z * 1000),  # Z axis control
            0,  # R (rotation)
            0   # Buttons
        )
        print(f"Control sent: x={x}, y={y}, z={z}")

# Example usage
if __name__ == "__main__":
    control = KeyboardControl('udp:127.0.0.1:14550')  # Example connection string
    input("Press Enter to exit...\n")
