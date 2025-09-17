import rclpy
from rclpy.node import Node
from mavros_msgs.msg import *
from std_msgs.msg import Float64

class Data_retrieve(Node):
    def __init__(self):
        super().__init__('data_retrieve')

        self.attittude_subscription_ = self.create_subscription(
            msg_type=Altitude,
            topic='/mavros/',
            callback=self.print_alt,
            qos_profile=10
        )

    def print_alt(self, msg):
        self.get_logger().info(f'atlitude : {msg.monotonic}')

def main(args=None):
    rclpy.init(args=args)
    node = Data_retrieve()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


# # ------------------------------------
# class Data_retrieve(Node):
#     def __init__(self):
#         super().__init__('data_retrieve')
#         self.altitude_subs = self.create_publisher(
#             msg_type=Float64,
#             topic = '/mavros/altitude',\
#             callback = self.print_alt,
#             qos_profile=10
#         )

#     def print_alt(self, msg):
#         self.get_logger().info(f'altitude : {msg.data}')

# def main(args=None):
#     rclpy.init(args=args)
#     node = Data_retrieve()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()