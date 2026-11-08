import tkinter as tk
from tkinter import filedialog, messagebox

# Store recorded keystrokes
keystrokes = []


# Function to record keyboard events
def record_key(event):

    # Ignore modifier keys
    if event.keysym in ["Shift_L", "Shift_R",
                        "Control_L", "Control_R",
                        "Alt_L", "Alt_R"]:
        return

    # Handle special keys
    if event.keysym == "Return":
        key = "[ENTER]"

    elif event.keysym == "BackSpace":
        key = "[BACKSPACE]"

    elif event.keysym == "space":
        key = "[SPACE]"

    elif event.char and event.char.isprintable():
        key = event.char

    else:
        return

    # Add the key to our list
    keystrokes.append(key)

    # Update the displayed count
    count_label.config(
        text=f"Keys recorded: {len(keystrokes)}"
    )


# Function to save recorded keystrokes
def save_log():

    if not keystrokes:
        messagebox.showwarning(
            "Warning",
            "No keystrokes recorded yet."
        )
        return

    # Ask the user where to save the file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:

        # Write recorded keys into a file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("Recorded Keystrokes:\n")
            file.write(" ".join(keystrokes))

        messagebox.showinfo(
            "Success",
            "Keystrokes saved successfully!"
        )


# Create application window
root = tk.Tk()

root.title("Keylogger Demonstration")
root.geometry("500x400")

# Application heading
heading = tk.Label(
    root,
    text="Keylogger Demonstration",
    font=("Arial", 16, "bold")
)
heading.pack(pady=10)

# Explain recording scope
notice = tk.Label(
    root,
    text="This application records only keys typed in the box below.",
    wraplength=450
)
notice.pack(pady=5)

# Text area for typing
text_box = tk.Text(
    root,
    height=10,
    width=50
)
text_box.pack(pady=10)

# Listen only to keyboard events in this text box
text_box.bind("<KeyPress>", record_key)

# Display recorded key count
count_label = tk.Label(
    root,
    text="Keys recorded: 0"
)
count_label.pack(pady=5)

# Save button
save_button = tk.Button(
    root,
    text="Save Keystrokes",
    command=save_log
)
save_button.pack(pady=10)

# Start application
root.mainloop()