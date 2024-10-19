import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

# Core Josephus formula as before
def josephus_formula(n):
    max_power_of_two = 1 << (n.bit_length() - 1)
    l = n - max_power_of_two
    return 2 * l + 1

# Visualization with enhanced circle resizing and elimination effects
def josephus_problem_visualization(n, canvas, fig, root):
    people = list(range(1, n + 1))  # Participants
    alive = [True] * n  # Alive tracker
    fig.clear()
    ax = fig.add_subplot(111)
    lines = []

    # Adjust the visualization dynamically based on the number of participants
    screen_height = root.winfo_screenheight()
    max_circle_diameter = 0.6 * screen_height
    circle_radius = max_circle_diameter / 2 / 100  # Scale for larger groups
    point_size = 8000 / n if n > 30 else 400  # Dynamically adjust size for readability

    # Function to update plot with visual indicators and dynamic adjustments
    def update_plot(alive, eliminator, eliminated, round_num):
        ax.clear()

        angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
        x = np.cos(angles) * circle_radius
        y = np.sin(angles) * circle_radius

        for i, person in enumerate(people):
            color = 'yellow' if alive[i] else 'grey'
            ax.scatter(x[i], y[i], s=point_size, color=color, edgecolors='black')
            ax.text(x[i], y[i], str(person), ha='center', va='center', color='black', fontsize=12)

            if not alive[i]:
                ax.text(x[i], y[i], 'X', ha='center', va='center', color='white', fontsize=16, fontweight='bold')

        # Draw the elimination line with dotted style for clarity
        if eliminator is not None and eliminated is not None:
            line, = ax.plot([x[eliminator], x[eliminated]], [y[eliminator], y[eliminated]], 
                            linestyle=':', color='blue', linewidth=1.5)
            lines.append(line)

        # Make previous lines fade for clarity in visual elimination tracking
        for line in lines:
            line.set_linestyle('--')
            line.set_color('blue')
            line.set_alpha(0.4)

        if eliminator is not None and eliminated is not None:
            ax.set_title(f"Round {round_num}: {people[eliminator]} eliminates {people[eliminated]}")
        else:
            ax.set_title(f"Final: {people[alive.index(True)]}" if alive.count(True) == 1 else f"Round {round_num}")

        ax.set_aspect('equal')
        ax.axis('off')

        canvas.draw()
        root.update()
        time.sleep(0.8)  # Slower delay for visibility of changes

    # Initial plot
    update_plot(alive, None, None, "Start")

    eliminator = 0
    round_num = 1

    while alive.count(True) > 1:
        eliminated = eliminator
        skipped = 0

        while skipped < 1 or not alive[eliminated]:
            eliminated = (eliminated + 1) % n
            if alive[eliminated]:
                skipped += 1

        # Mark the person as eliminated
        alive[eliminated] = False
        update_plot(alive, eliminator, eliminated, round_num)
        round_num += 1

        eliminator = (eliminated + 1) % n
        while not alive[eliminator]:
            eliminator = (eliminator + 1) % n

    # Final plot for the last person standing
    update_plot(alive, eliminator, None, "Final")

# GUI setup with input for participants and buttons
def on_start():
    n = int(entry.get())
    josephus_problem_visualization(n, canvas, fig, root)

root = tk.Tk()
root.title("Josephus Problem Visualization")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Input field for number of people and Start button
input_frame = ttk.Frame(frame)
input_frame.grid(row=0, column=0, sticky="ew")
ttk.Label(input_frame, text="Enter number of people:").grid(row=0, column=0, padx=5, pady=5)
entry = ttk.Entry(input_frame, width=10)
entry.grid(row=0, column=1, padx=5, pady=5)
start_button = ttk.Button(input_frame, text="Start", command=on_start)
start_button.grid(row=0, column=2, padx=5, pady=5)

# Matplotlib figure embedded in Tkinter window
fig = plt.Figure(figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew")

frame.rowconfigure(1, weight=1)
frame.columnconfigure(0, weight=1)

root.mainloop()