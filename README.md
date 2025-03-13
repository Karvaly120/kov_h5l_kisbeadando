# Billentyűzetes Robotvezérlés

Ez a projekt egy egyszerű ROS 2 csomag (keyboard_control), amely lehetővé teszi a robot vezérlését billentyűleütések segítségével. A csomag két fő node-ból áll: egy publisher és egy subscriber node-ból.

## Fájlok
- **keyboard_publisher.py**: Figyeli a billentyűleütéseket, és a megfelelő vezérlési parancsokat elküldi a 'cmd_vel' témára.
- **command_subscriber.py**: Feliratkozik a 'cmd_vel' témára, és kiírja a kapott vezérlési parancsokat.
- **launch/keyboard_control_launch.py**: Egyszerre indítja el a két node-ot külön terminálablakban.

## Telepítés
1. Készítsd el a ROS 2 munkakörnyezetet:
   ```bash
   cd ~/ros2_ws/src
   ```
2. Klónozd a projektet vagy helyezd a forráskódot a `src` könyvtárba.
   ```bash
   git clone https://github.com/Karvaly120/kov_h5l_kisbeadando
   ```   
3. Lépj vissza a munkakönyvtárba:
   ```bash
   cd ~/ros2_ws
   ```
4. Buildeld a csomagot:
   ```bash
   colcon build --packages-select keyboard_control
   ```
   <details>
   <summary> Don't forget to source before ROS commands.</summary>

   ``` bash
   source ~/ros2_ws/install/setup.bash
   ```
</details>

## Használat
1. Indítsd el a billentyűzetes vezérlő node-ot:
   ```bash
   ros2 launch keyboard_control keyboard_control_launch.py
   ```

   ## Program működése

## Graph

Az alábbi diagram szemlélteti a billentyűzetes robotvezérlés működését:

```mermaid
graph LR;

pub([ /keyboard_publisher]):::red --> cmd_vel[ /cmd_vel<br/>std_msgs/String]:::light
cmd_vel --> sub([ /command_subscriber]):::red

classDef light fill:#34aec5,stroke:#152742,stroke-width:2px,color:#152742  
classDef dark fill:#152742,stroke:#34aec5,stroke-width:2px,color:#34aec5
classDef white fill:#ffffff,stroke:#152742,stroke-width:2px,color:#152742
classDef red fill:#ef4638,stroke:#152742,stroke-width:2px,color:#fff
```


![](img/mukodes.png)
