import rclpy
from rclpy.node import Node
# from mavros_msgs.msg import DistanceSensor
from mavros_msgs.msg import Altitude


class Anti_collision(Node):
    def __init__(self):
        super().__init__('anti_collision')
        # self.lidar_ = self.create_subscription(
        #     msg_type=DistanceSensor,
        #     topic='altitude',
        #     callback=self.get_range(),
        #     qos_profile=10
        # )
        self.altitude_ = self.create_subscription(
            msg_type=Altitude,
            topic='/mavros/altitude',
            callback=self.get_alt,
            qos_profile=10
        )
        self.get_logger().info('node started')
    
    # def get_range(self, msg):
    #     range = msg.current_distance
    #     self.get_logger().info(f'range : {range}')

    def get_alt(self,msg):
        alt = msg.terrain
        self.get_logger().info(f'altitude : {alt}')
        

def main(args=None):
    rclpy.init(args=args)
    node = Anti_collision()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()