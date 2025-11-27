# COM 3524 Group Project - Forest Fire Simulation

This repository contains the adapted Cellular Automata (CA) model used to simulate wildfire spread across heterogenous terrain, based on the COM3524 "Bio-Inspired Computing" assignment brief.

This project investigates how fire spreads from two industrial ignition sources, a power plant and an incinerator, towards a nearby town, under different environmental conditions.

## Prerequisites
To run the simulation, you need:

- [Python 3.8+](https://www.python.org/downloads/)
- [NumPy]
- CAPyle CA Simulator (provided in the module)
- `pip` (Python package manager for installing necessary dependencies)
- Git (to clone this repository)

## Running the Simulation (Using CAPlye GUI)

### 1. Launch the tools menu
Inside the COM3524 container, run:

```bash
python run_tool.py 
```
---

Once you run the command, the following menu should appear, allowing you to select which tool to launch.

<div style="display: flex; align-items: flex-start; gap: 1rem;">

  <img src="https://github.com/user-attachments/assets/62b99fdb-c21e-4d47-add8-1b6166f2dda6" alt="Tools Menu Screenshot" width="500" style="border-radius: 8px;">
</div>

  - The menu allows you to select from available tools.
  - Use the number keys (1–3) to choose the desired tool.  
  - Choose number 3 (CAPyle Tool) to open the CAPyle GUI.

### 2. Load the Wildfire Model

In the CAPyle interface;

- Go to File → Open
- Select the file: 

```bash
forest.py 
```

- Go to Simulation → Run Configuration
- Start the simulation by clicking the play button.

### 3. Choosing the Ignition Scenario
The ignition point is controlled in forest.py inside the setup() function.

#### Power Plant Ignition (Scenario 1)
Ensure you have:

```bash
initial_grid[1, 5] = 9
```
This puts a burning cell near the power plant

#### Incinerator Ignition (Scenario 1)
Ensure you have:

```bash
initial_grid[1, 49] = 9
```
This puts a burning cell near the incinerator

### 4. Running Wind Scenarios

### 5. Running Intervention Scenarios


## Author
Ayesha Sana, Department of Computer Science  
