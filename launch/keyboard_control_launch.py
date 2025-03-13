from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['xterm', '-fa', 'Monospace', '-fs', '10', '-hold', '-e', 'ros2 run keyboard_control keyboard_publisher'],
            name='keyboard_publisher_terminal'
        ),
        ExecuteProcess(
            cmd=['xterm', '-fa', 'Monospace', '-fs', '10', '-hold', '-e', 'ros2 run keyboard_control command_subscriber'],
            name='command_subscriber_terminal'
        ),
    ])