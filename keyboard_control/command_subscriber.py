import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommandSubscriber(Node):
    def __init__(self):
        super().__init__('command_subscriber')
        self.subscription = self.create_subscription(
            String,
            'commands',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        commands = {
            'w': 'Előre',
            'a': 'Balra',
            's': 'Hátra',
            'd': 'Jobbra'
        }
        self.get_logger().info(f'Megkapott parancs: {commands.get(msg.data, "Ismeretlen")}')
        
def main(args=None):
    rclpy.init(args=args)
    node = CommandSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
