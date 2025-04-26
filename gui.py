import tkinter as tk
from tkinter import messagebox
import random
import subprocess
import os
from core import get_trigram, get_changed_lines, get_hexagram_result

# Generate original and changed hexagrams from the three user inputs 
def gui_generate_hexagram(n1, n2, n3):
    # inputs: integers; outputs: strings with result and interpretation
    upper = get_trigram(n1 % 8)
    lower = get_trigram(n2 % 8)
    original = f"{upper}\n{lower}"
    changed = get_changed_lines(original, n3 % 6)
    return original, changed, get_hexagram_result(original), get_hexagram_result(changed)

# Launch the turtle graphic to generate number
def run_turtle_and_get_number(target_index, speed_choice):
    #Run turtle program, return generated number for the selected entry (first, second, or third numeber input)
    temp_file = "turtle_result.txt"
    if os.path.exists(temp_file):
        os.remove(temp_file)
    subprocess.run(["python3", "turtle_num_generator.py", str(target_index), speed_choice])
    if os.path.exists(temp_file):
        with open(temp_file, "r") as f:
            try:
                index, value = f.read().strip().split(":")
                return int(index), int(value)
            except:
                return None, None
    return None, None

# Popup for turtle generator options
def ask_turtle_options():
    #Popup window for user select which number to generate and turtle speed (if they want a smaller number, slow; fast for bigger numbers)
    global entries #globalize the entries to use throughout
    popup = tk.Toplevel()
    popup.title("Turtle Setup")

    tk.Label(popup, text="The turtle will wander randomly.\n Press SPACE to stop it.\nThe farther it moves before you press SPACE,\nthe bigger your number will be!").pack(pady=10)

    # Buttons for the user to choose which number to generate
    number_var = tk.IntVar(value=0)
    tk.Label(popup, text="Which number do you want to fill?").pack()
    tk.Radiobutton(popup, text="First Number", variable=number_var, value=0).pack()
    tk.Radiobutton(popup, text="Second Number", variable=number_var, value=1).pack()
    tk.Radiobutton(popup, text="Third Number", variable=number_var, value=2).pack()

    # Buttons for speed choice
    tk.Label(popup, text="Choose Turtle Speed:").pack()
    speed_var = tk.StringVar(value="medium")
    tk.Radiobutton(popup, text="Slow", variable=speed_var, value="slow").pack()
    tk.Radiobutton(popup, text="Medium", variable=speed_var, value="medium").pack()
    tk.Radiobutton(popup, text="Fast", variable=speed_var, value="fast").pack()

    # Confirm the user's choices and run turtle
    def on_confirm():
        idx = number_var.get()
        spd = speed_var.get()
        popup.destroy()
        idx, result = run_turtle_and_get_number(idx, spd)
        if result is not None:
            entries[idx].delete(0, tk.END)
            entries[idx].insert(0, result)
        else:
            messagebox.showerror("Error", "Turtle did not return a valid number.")

    tk.Button(popup, text="Start Turtle!", command=on_confirm).pack(pady=10)

# Setup and run the gui
def run_gui():
    #Function to create and control the gui
    root = tk.Tk()
    root.title("Six Lines Divination (I Ching)")

    tk.Label(root, text="Enter 3 three-digit numbers:").grid(row=0, column=0, columnspan=3, pady=5)

    global entry1, entry2, entry3, entries
    entry1 = tk.Entry(root, width=10)
    entry2 = tk.Entry(root, width=10)
    entry3 = tk.Entry(root, width=10)
    entry1.grid(row=1, column=0, padx=5)
    entry2.grid(row=1, column=1, padx=5)
    entry3.grid(row=1, column=2, padx=5)
    entries = [entry1, entry2, entry3]

    # Use input numbers to generate hexagrams
    def on_generate():
        #Use the entries to generate and display the divination result
        try:
            n1 = int(entry1.get())
            n2 = int(entry2.get())
            n3 = int(entry3.get())
            if not (100 <= n1 <= 999 and 100 <= n2 <= 999 and 100 <= n3 <= 999):
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter three-digit numbers only.")
            return

        original, changed, msg1, msg2 = gui_generate_hexagram(n1, n2, n3)
        result_text.set(f"Original 6 lines:\n{original}\n\nResult:\n{msg1}\n\n"
                        f"Changed 6 lines:\n{changed}\n\nResult:\n{msg2}")

    #Fill inputs with random numbers if the user chooses to do so
    def on_random():
        #Randomly fill the three input fields with numbers 100–999
        for e in [entry1, entry2, entry3]:
            e.delete(0, tk.END)
            e.insert(0, random.randint(100, 999))

    #Clear all input fields
    def on_clear():
        #Clear all 3 input fieflds
        for e in [entry1, entry2, entry3]:
            e.delete(0, tk.END)

    # gui buttons
    tk.Button(root, text="Generate", command=on_generate).grid(row=2, column=0, pady=10)
    tk.Button(root, text="Random", command=on_random).grid(row=2, column=1, pady=10)
    tk.Button(root, text="Clear", command=on_clear).grid(row=2, column=2, pady=10)
    tk.Button(root, text="Use Turtle Generator", command=ask_turtle_options).grid(row=3, column=0, columnspan=3, pady=10)

    # show results
    result_text = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_text, justify="left", font=("Courier", 10))
    result_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
