import tkinter as tk
from tkinter import messagebox
import random
from core import get_trigram, get_changed_lines, get_hexagram_result

def gui_generate_hexagram(n1, n2, n3):
    upper = get_trigram(n1 % 8)
    lower = get_trigram(n2 % 8)
    original = f"{upper}\n{lower}"
    changed = get_changed_lines(original, n3 % 6)
    return original, changed, get_hexagram_result(original), get_hexagram_result(changed)

def run_gui():
    def on_generate():
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

    def on_random():
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        nums = [random.randint(100, 999) for _ in range(3)]
        entry1.insert(0, nums[0])
        entry2.insert(0, nums[1])
        entry3.insert(0, nums[2])

    root = tk.Tk()
    root.title("Six Lines Divination (I Ching)")

    tk.Label(root, text="Enter 3 three-digit numbers:").grid(row=0, column=0, columnspan=3, pady=5)

    entry1 = tk.Entry(root, width=10)
    entry2 = tk.Entry(root, width=10)
    entry3 = tk.Entry(root, width=10)
    entry1.grid(row=1, column=0, padx=5)
    entry2.grid(row=1, column=1, padx=5)
    entry3.grid(row=1, column=2, padx=5)

    tk.Button(root, text="Generate", command=on_generate).grid(row=2, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Random", command=on_random).grid(row=2, column=2, pady=10)

    result_text = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_text, justify="left", font=("Courier", 10))
    result_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
