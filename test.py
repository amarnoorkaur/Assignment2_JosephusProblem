import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

# We're keeping the Josephus logic from before
def josephus_formula(n):
    max_power_of_two = 1 << (n.bit_length() - 1)
    l = n - max_power_of_two
    return 2 * l + 1

# Setting up a basic visualization inside a Tkinter window
def josephus_problem_visualization(n, canvas, fig, root):
    people = list(range(1, n + 1))  # Circle of people
    alive = [True] * n  # Who’s still alive

    fig.clear()  # Clear any previous figure
    ax = fig.add_subplot(111)

    # Function to update the plot during each elimination round
    def update_plot(eliminator, eliminated, alive, round_num):
        ax.clear()  # Clear old plot

        # Calculate the circle positions
        angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
        x = np.cos(angles)
        y = np.sin(angles)

        # Plot each person in the circle
        for i in range(n):
            color = 'yellow' if alive[i] else 'grey'  # Alive = yellow, Dead = grey
            ax.scatter(x[i], y[i], s=500, color=color, edgecolors='black')
            ax.text(x[i], y[i], str(people[i]), ha='center', va='center', color='black')

        # Draw elimination line
        if eliminator is not None and eliminated is not None:
            ax.plot([x[eliminator], x[eliminated]], [y[eliminator], y[eliminated]], 'r--')

        ax.set_title(f"Round {round_num}: Eliminator {people[eliminator]} -> Eliminated {people[eliminated]}" if eliminator is not None else "Starting Position")
        ax.set_aspect('equal')
        ax.axis('off')

        canvas.draw()
        root.update()
        time.sleep(1)  # Delay for visual clarity

    # Initial plot
    update_plot(None, None, alive, "Start")

    # Elimination logic: Just like we did before
    eliminator = 0
    round_num = 1
    while alive.count(True) > 1:
        eliminated = eliminator
        skipped = 0
        
        while skipped < 1 or not alive[eliminated]:
            eliminated = (eliminated + 1) % n
            if alive[eliminated]:
                skipped += 1

        alive[eliminated] = False  # Mark the person as eliminated
        update_plot(eliminator, eliminated, alive, round_num)  # Update visualization

        # Move to next round
        round_num += 1
        eliminator = (eliminated + 1) % n
        while not alive[eliminator]:
            eliminator = (eliminator + 1) % n

    # Final round
    update_plot(eliminator, None, alive, "Final")

# GUI Setup with Tkinter
def on_start():
    n = int(entry.get())  # Grab user input
    josephus_problem_visualization(n, canvas, fig, root)  # Run the visualization

root = tk.Tk()
root.title("Josephus Problem Visualization")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Input field and Start button
input_frame = ttk.Frame(frame)
input_frame.grid(row=0, column=0, sticky="ew")
ttk.Label(input_frame, text="Enter number of people:").grid(row=0, column=0, padx=5, pady=5)
entry = ttk.Entry(input_frame, width=10)
entry.grid(row=0, column=1, padx=5, pady=5)
start_button = ttk.Button(input_frame, text="Start", command=on_start)
start_button.grid(row=0, column=2, padx=5, pady=5)

# Matplotlib figure setup inside the Tkinter window
fig = plt.Figure(figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew")

frame.rowconfigure(1, weight=1)
frame.columnconfigure(0, weight=1)

root.mainloop()