import rclpy
from rclpy.node import Node
from mavros_msgs.msg import OpticalFlow


class Opflow(Node):
    def __init__(self):
        super().__init__('opflow_read')
        
        # create opflow subscription
        self.opflow_subs = self.create_subscription(
            msg_type=OpticalFlow,
            topic='opflow',
            callback=self.print_opflow,
            qos_profile=10
        )

    def print_opflow(self, msg):
        self.get_logger().info(
            f'alt = {msg.ground_distance}\nflow x = {msg.flow_comp_m}\n')

def main(args=None):
    rclpy.init(args=args)
    node = Opflow()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()