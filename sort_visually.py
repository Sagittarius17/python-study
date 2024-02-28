import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint
import tkinter as tk

# Function to generate random data for sorting
def generate_data(size=50):
    return [randint(1, 100) for _ in range(size)]

# Function to perform bubble sort
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                yield data, (j, j+1)

# Function to update plot
def update_plot(frame, bars, text):
    data, (i, j) = frame
    for bar, val in zip(bars, data):
        bar.set_height(val)
    text.set_text(f"Comparing elements: {data[i]} and {data[j]}")
    return bars, text

# Function to start sorting animation
def start_sort():
    data = generate_data()
    generator = bubble_sort(data)

    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort Visualization")
    ax.set_xticks([])
    ax.set_yticks([])

    bars = ax.bar(range(len(data)), data, align="edge")
    comparison_text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update(frame):
        data, (i, j) = frame
        for bar, val in zip(bars, data):
            bar.set_height(val)
        comparison_text.set_text(f"Comparing elements: {data[i]} and {data[j]}")

    anim = animation.FuncAnimation(fig, update, frames=generator, interval=50, repeat=False)
    plt.show()
# GUI
root = tk.Tk()
root.title("Sorting Visualization")

sort_button = tk.Button(root, text="Sort", command=start_sort)
sort_button.pack()

root.mainloop()
