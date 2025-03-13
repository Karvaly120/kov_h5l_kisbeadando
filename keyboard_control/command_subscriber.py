import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommandSubscriber(Node):
    def __init__(self):
        super().__init__('command_subscriber')
        self.subscription = self.create_subscription(
            String,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Várakozás parancsokra...')

    def listener_callback(self, msg):
        directions = {'w': 'Előre megy', 's': 'Hátra megy', 'a': 'Balra fordul', 'd': 'Jobbra fordul'}
        direction = directions.get(msg.data, 'Ismeretlen parancs')
        self.get_logger().info(f'Megkapott parancs: {msg.data} -> {direction}')

def main(args=None):
    rclpy.init(args=args)
    node = CommandSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()