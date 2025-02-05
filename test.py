import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

# Josephus formula function with detailed breakdown
def josephus_formula_detailed(n):
    largest_power_of_two = 1 << (n.bit_length() - 1)
    l = n - largest_power_of_two
    winning_position = 2 * l + 1
    return winning_position, largest_power_of_two, l

# Binary rotation function
def binary_rotation(n):
    binary_str = bin(n)[2:]
    rotated_binary_str = binary_str[1:] + binary_str[0]
    rotated_decimal = int(rotated_binary_str, 2)
    return rotated_decimal, binary_str, rotated_binary_str

# Josephus visualization with optimized layout and UI
def josephus_problem_visualization(n, canvas, fig, formula_label, binary_label, root):
    people = list(range(1, n + 1))
    alive = [True] * n
    fig.clear()
    ax = fig.add_subplot(111)
    lines = []

    # Set dynamic sizing for readability
    screen_height = root.winfo_screenheight()
    max_circle_diameter = 0.8 * screen_height  # Optimize figure to take 80% of screen height
    circle_radius = max_circle_diameter / 2 / 100
    point_size = 8000 / n if n > 30 else 600

    def update_plots(alive, round_num, eliminator, eliminated):
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

        # Dotted line to show who eliminates whom
        if eliminator is not None and eliminated is not None:
            line, = ax.plot([x[eliminator], x[eliminated]], 
                            [y[eliminator], y[eliminated]], 
                            linestyle=':', color='blue', linewidth=2)
            lines.append(line)

        for line in lines:
            line.set_linestyle('-')
            line.set_alpha(0.5)

        # Update title based on elimination round or final result
        if eliminator is not None and eliminated is not None:
            ax.set_title(f"Round {round_num}: {people[eliminator]} eliminates {people[eliminated]}", fontsize=16)
        else:
            ax.set_title(f"Final: {people[alive.index(True)]}", fontsize=16)

        ax.set_aspect('equal')
        ax.axis('off')

        # Josephus formula breakdown displayed
        winner_formula, largest_power_of_two, l = josephus_formula_detailed(n)
        formula_text = (f"Given n = {n}, find largest 2^a ≤ n:\n"
                        f"2^a = {largest_power_of_two}\n"
                        f"Then, l = n - 2^a = {n} - {largest_power_of_two} = {l}\n"
                        f"Winning Position: W(n) = 2 * {l} + 1 = {winner_formula}")
        formula_label.config(text=f"Josephus Formula\n{formula_text}")

        # Binary rotation breakdown displayed
        winner_binary, original_binary, rotated_binary = binary_rotation(n)
        binary_text = (f"Original: {original_binary}\n"
                       f"Rotated: {rotated_binary}\n"
                       f"Binary Winner: {winner_binary}")
        binary_label.config(text=f"Binary Rotation\n{binary_text}")

        canvas.draw()
        root.update_idletasks()
        root.update()
        time.sleep(0.8)

    # Initial plot
    update_plots(alive, "Start", None, None)

    eliminator = 0
    round_num = 1

    while alive.count(True) > 1:
        eliminated = eliminator
        skipped = 0

        while skipped < 1 or not alive[eliminated]:
            eliminated = (eliminated + 1) % n
            if alive[eliminated]:
                skipped += 1

        alive[eliminated] = False
        update_plots(alive, round_num, eliminator, eliminated)
        round_num += 1
        time.sleep(0.7)

        eliminator = (eliminated + 1) % n
        while not alive[eliminator]:
            eliminator = (eliminator + 1) % n

    update_plots(alive, "Final", eliminator, None)

# Refined layout with improved spacing and design
def on_start():
    n = int(entry.get())
    josephus_problem_visualization(n, canvas, fig, formula_label, binary_label, root)

# Tkinter window setup with optimized UI layout
root = tk.Tk()
root.title("Josephus Problem Visualization")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Input area setup
input_frame = ttk.Frame(frame)
input_frame.grid(row=0, column=0, sticky="ew")

ttk.Label(input_frame, text="Enter number of people:").grid(row=0, column=0, padx=5, pady=5)
entry = ttk.Entry(input_frame, width=10)
entry.grid(row=0, column=1, padx=5, pady=5)
start_button = ttk.Button(input_frame, text="Start", command=on_start)
start_button.grid(row=0, column=2, padx=5, pady=5)

# Side panel for explanations
side_frame = ttk.Frame(frame)
side_frame.grid(row=1, column=1, sticky="ns", padx=10)

# Josephus formula explanation with larger font
formula_label = ttk.Label(side_frame, text="Josephus Formula", font=("Arial", 12, "bold"), padding="10", justify="left", relief="groove")
formula_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Binary rotation explanation with panel borders for separation
binary_label = ttk.Label(side_frame, text="Binary Rotation", font=("Arial", 12, "bold"), padding="10", justify="left", relief="groove")
binary_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# Main figure area for the circular visualization
fig = plt.Figure(figsize=(12, 10))
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew")

frame.rowconfigure(1, weight=1)
frame.columnconfigure(0, weight=1)

root.mainloop()
