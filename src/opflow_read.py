from pymavlink import mavutil

port = "/dev/ttyACM0"
baudrate = 115200

fc = mavutil.mavlink_connection(device=port, baud=baudrate)
fc.wait_heartbeat()

print(f'heartbeat detected. system = {fc.target_system}; component = {fc.target_component}')

message = fc.mav.command_long_encode(
    fc.target_system,   # target system
    fc.target_component, # target component
    mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL, # ID of command to send
    0, # confirmation
    mavutil.mavlink.MAVLINK_MSG_ID_OPTICAL_FLOW, # param 1 : message ID
    100000, # param 2 : interval in usec
    0, 0, 0, 0, 0 # param 3 - 7 (not used)
)

fc.mav.send(message)

while True:
    response = fc.recv_match(type="OPTICAL_FLOW", blocking=True, timeout=5.0)
    if response:
        velx = response.flow_comp_m_x``
        vely = response.flow_comp_m_y
        alt = response.ground_distance

        print(f'velx = {velx}')
        print(f'vely = {vely}')
        print(f'alt = {alt}')
