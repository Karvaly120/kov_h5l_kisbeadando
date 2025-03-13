cmake_minimum_required(VERSION 3.8)
project(keyboard_control)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

# Találja meg a szükséges csomagokat
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

# Python fájlok telepítése
install(PROGRAMS
  keyboard_publisher.py
  command_subscriber.py
  DESTINATION lib/${PROJECT_NAME}
)

# Launch fájlok telepítése
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

# Ament csomag létrehozása
ament_package()
