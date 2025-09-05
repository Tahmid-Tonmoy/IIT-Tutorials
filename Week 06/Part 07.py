import tkinter as tk

def calculate_result():
    try:
        # Get input values
        m1 = float(entry1.get())
        m2 = float(entry2.get())
        m3 = float(entry3.get())

        # Calculate average
        avg = (m1 + m2 + m3) / 3

        # Pass/Fail check
        if avg >= 50:
            result_label.config(text=f"Average: {avg:.2f} - Passed")
        else:
            result_label.config(text=f"Average: {avg:.2f} - Failed")

    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Student Result Calculator")
root.geometry("300x200")

# Labels and text boxes
tk.Label(root, text="Enter Mark 1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Mark 2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Enter Mark 3:").pack()
entry3 = tk.Entry(root)
entry3.pack()

# Button
tk.Button(root, text="Calculate Result", command=calculate_result).pack(pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Run the app
root.mainloop()
