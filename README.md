# UUV Simulation

A Python-based numerical simulation of an **Unmanned Underwater Vehicle (UUV)** to model and visualize its dynamics under varying water currents and control inputs.

This project implements the **6-DOF (Degrees of Freedom) equations of motion** for underwater vehicles, simulates trajectory tracking based on waypoints, and visualizes results such as velocity, orientation, and control responses.

## 🚀 Features

* Pure Python implementation.
* Implements **mathematical models** for UUV motion including hydrodynamic forces, added mass, and control surface effects.
  
* Simulates:
  * Vehicle states (position, orientation, velocity).
  * Control surface responses (rudder, stern plane, propeller).
  * Effect of water current speed and direction.
    
* Generates detailed plots for analysis:
  * State evolution (velocities, angular rates, Euler angles).
  * Control commands vs. responses.
  * **3D trajectory visualization** of the UUV path.

## 📂 Project Structure

```
Uw-Sim/
│── python_vehicle_simulator     # Core simulation script
│── Last_Profile.csv             # Input parameters file for core simulation
│── main.py                      # main file which runs the script with input parameters
│── outupt.csv                   # Final output value in .csv file format
│── README.md                    # Documentation
```

## 🛠️ Requirements

* Python 3.8+
* Install dependencies:

```bash
pip install -r requirements.txt
```

Typical requirements:

* `numpy`
* `matplotlib`
* `pandas`

## ▶️ Running the Simulation

Run the simulation with:

```bash
python uuv_simulation.py
```

Provide waypoints in the script, and the vehicle will generate trajectories and state plots based on the inputs.

## 📊 Outputs

### 1. Vehicle States
Plots showing linear velocities, angular velocities, Euler angles (roll, pitch, yaw), and depth changes.

### 2. Control Surfaces
Graphs of **rudder angle**, **stern plane angle**, and **propeller speed**, reflecting the UUV’s control responses against inputs.

### 3. 3D Trajectory
A 3D visualization of the UUV’s path through water while tracking waypoints under current disturbances.

![uuv_simlution_pic1](https://github.com/user-attachments/assets/e2a98546-4db9-4016-8782-eeb2edbc8774)
![uuv_simulation_pic2](https://github.com/user-attachments/assets/93d759d7-452d-475b-8438-9d7138e71063)
![uuv_simulation_pic3](https://github.com/user-attachments/assets/918f5aac-0850-417a-9b4c-3048090de2e7)


## 📜 License
This project is licensed under the **MIT License**.
