import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class KeyboardPublisher(Node):
    def __init__(self):
        super().__init__('keyboard_publisher')
        self.publisher_ = self.create_publisher(String, 'commands', 10)
        self.get_logger().info('Billentyűzetfigyelő elindult. Használj W, A, S, D billentyűket!')

    def publish_command(self, key):
        msg = String()
        if key in ['w', 'a', 's', 'd']:
            msg.data = key
            self.publisher_.publish(msg)
            self.get_logger().info(f'Küldött parancs: {key}')

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardPublisher()
    try:
        while True:
            key = input('Adj meg egy irányt (W/A/S/D): ').lower()
            node.publish_command(key)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
