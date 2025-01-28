# Disk-Scheduling-Algorithms-Simulation-with-GUI.
Key Features
Algorithms Implemented:

FCFS (First Come, First Serve): Processes requests in the order they arrive.
SSTF (Shortest Seek Time First): Processes the closest request to the current disk head position.
SCAN (Elevator Algorithm): Moves the head in one direction, servicing requests, then reverses.
C-SCAN (Circular SCAN): Similar to SCAN but wraps around to the other end after reaching the boundary.
LOOK and C-LOOK: Variants of SCAN and C-SCAN that don’t move the head to the boundary unless needed.
Graphical Visualization:

Disk head movement is displayed using Turtle Graphics, showing the order in which requests are serviced.
A bar graph compares the total head movements across all algorithms.
GUI Features:

Drop-down menu to select the desired disk scheduling algorithm.
Input fields for the initial head position and disk track requests.
Buttons for simulating the head movement and generating comparative graphs.
Statistics:

Displays total head movement and average track movement for each simulation.
How It Works
GUI Setup:

The main window (Main) contains labels, entry fields, and buttons for user interaction.
Users can input:
A list of disk requests (track numbers).
The starting position of the disk head.
Select an algorithm from a drop-down menu.
Execution Flow:

When the "Simulate head movement" button is clicked:
The program calls the selected algorithm to calculate the servicing order and total head movement.
The results are visualized using Turtle Graphics.
When the "Make a Statistic Graph" button is clicked:
The program calculates the total head movements for all algorithms and displays them in a bar graph.
Algorithms:

Each algorithm computes:
The order of servicing requests.
The total head movement (sum of absolute differences between consecutive positions).
The results are stored and used for visualization.
Visualization:

Turtle Graphics: Shows the path of the disk head and marks serviced tracks.
Matplotlib: Plots the total head movements for comparison across algorithms.
Modules Used
Tkinter: For GUI components (labels, buttons, text fields).
Turtle: For step-by-step disk head movement visualization.
Matplotlib: For generating comparative graphs.
NumPy and Pandas: Auxiliary tools for data manipulation (though sparsely used).
