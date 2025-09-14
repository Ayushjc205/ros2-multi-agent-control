# ROS2 Multi-Agent Control Using Turtlesim

This project demonstrates multi-agent control in ROS2 using the `turtlesim` simulator.  
It implements a system where multiple turtles are spawned dynamically in the environment and a controller selects and catches the nearest turtle using custom logic.

# ✨ Features
- 🐢 **Dynamic spawning** of turtles using a dedicated spawner node.  
- 🎯 **Nearest target selection** and control logic implemented in the controller node.  
- 📡 **Custom ROS2 interfaces** (`msg` and `srv`) for inter-node communication.  
- ⚡ **Launch file** to start the complete multi-agent setup with a single command.  
- 🔧 Easily configurable parameters (e.g., spawn behavior, control rates).

# 📂 Project Structure
ros2-multi-agent-control/
├── src/
│ ├── multi_agent_bringup/ # Launch and config files
│ ├── multi_agent_control/ # Core logic (controller & spawner)
│ └── multi_agent_interfaces/ # Custom messages and services
├── build/ # Build output (ignored in git)
├── install/ # Install space (ignored in git)
├── log/ # Logs (ignored in git)
└── README.md

# Key Nodes
- `turtlesim_spawner.py` → Spawns turtles dynamically in the simulation.  
- `turtlesim_controller.py` → Control algorithm to chase and catch the nearest turtle.
# Launch Command
ros2 launch multi_agent_bringup multi_agent_control.launch.xml
