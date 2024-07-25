# waypoint_interface.py

from pymavlink import mavutil

class WaypointInterface:
    def __init__(self, connection_string):
        self.mav = mavutil.mavlink_connection(connection_string)
        self.mav.wait_heartbeat()

    def send_waypoint(self, lat, lon, alt):
        # Send MAVLink waypoint message
        self.mav.mav.mission_item_send(
            0,  # Target system
            0,  # Target component
            0,  # Sequence number
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
            mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
            0,  # Current
            0,  # Autocontinue
            0, 0, 0, 0,  # Reserved
            lat,  # Latitude
            lon,  # Longitude
            alt   # Altitude
        )
        print(f"Waypoint sent: lat={lat}, lon={lon}, alt={alt}")

# Example usage
if __name__ == "__main__":
    waypoint_interface = WaypointInterface('udp:127.0.0.1:14550')  # Example connection string
    waypoint_interface.send_waypoint(37.7749, -122.4194, 100)  # Send waypoint to San Francisco
