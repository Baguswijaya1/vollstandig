from pymavlink import mavutil

serial_port = '/dev/ttyACM0'
baud_rate = 115200
mavlink_connection = mavutil.mavlink_connection(serial_port, baud=baud_rate)

#heartbeat
mavlink_connection.wait_heartbeat()
print(f"Heartbeat from system (system {mavlink_connection.target_system} component {mavlink_connection.target_component})")

def request_message_interval(master, message_input: str, frequency_hz: float):
    message_name = "MAVLINK_MSG_ID_" + message_input
    message_id = getattr(mavutil.mavlink, message_name)
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,
        0, message_id, 1e6 / frequency_hz, 0, 0, 0, 0, 0
    )
    print(f"Requested {message_input} at {frequency_hz} Hz")

request_message_interval(mavlink_connection, "GLOBAL_POSITION_INT", 5.0)

while True:
    message = mavlink_connection.recv_match(type="GLOBAL_POSITION_INT", blocking=True, timeout=1.0)
    if message:
        latitude = message.lat / 1e7
        longitude = message.lon / 1e7
        altitude = message.alt # mm atau m 

        print(f"\nLatitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"Altitude: {altitude} m")
