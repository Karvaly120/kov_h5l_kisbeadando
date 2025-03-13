from setuptools import find_packages, setup

package_name = 'keyboard_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ajr',
    maintainer_email='karvaly120@gmail.com',
    description='billenytűzetes robot vezérlés',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'keyboard_publisher = keyboard_control.keyboard_publisher:main',
            'command_subscriber = keyboard_control.command_subscriber:main',
        ],
    },
)
