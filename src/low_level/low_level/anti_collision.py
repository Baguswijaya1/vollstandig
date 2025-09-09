import rclpy
from rclpy.node import Node
from mavros_msgs.msg import Altitude
from mavros_msgs.msg import *

class Anti_collision(Node):
    def __init__(self):
        super().__init__('anti_collision')
        lidar_ = self.create_subscription(
            msg_type=Altitude,
            topic='altitude',
            callback=self.altitude_action(),
            qos_profile=10
        )

    def altitude_action(self, msg):
        terrain_altitude = msg.terrain_altitude
        self.get_logger().info(f'terrain altitude = {terrain_altitude}'))

def main(args=None):
    rclpy.init(args=args)
    node = Anti_collision()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    try:
        main()
    except:
        Anti_collision.get_logger().info('something wrong')