import tkinter as tk
from tkinter import messagebox, filedialog
from bus_stop_controller import BusStopController

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Stop Navigator")
        self.controller = None

        # UI elements
        self.label = tk.Label(root, text="Load Bus Stops Data:")
        self.label.pack(pady=10)

        self.load_button = tk.Button(root, text="Load CSV", command=self.load_csv)
        self.load_button.pack(pady=5)

        self.find_next_button = tk.Button(root, text="Find Next Stops", command=self.find_next_stops)
        self.find_next_button.pack(pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=20)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.controller = BusStopController(file_path)
            messagebox.showinfo("Info", "Bus stops loaded successfully!")

    def find_next_stops(self):
        if not self.controller:
            messagebox.warning(self, "Warning", "Please load bus stop data first.")
            return

        next_stops = self.controller.get_next_stops()
        if next_stops:
            stop_descriptions = "\n".join([f"{stop.description} (ID: {stop.object_id})" for stop in next_stops])
            selected_stop = self.prompt_for_stop_selection(stop_descriptions)
            if selected_stop:
                self.controller.set_current_stop(selected_stop)
                messagebox.showinfo("Info", f"Moved to {self.controller.current_stop.description}!")
        else:
            messagebox.information(self, "Info", "No next stops found.")

    def prompt_for_stop_selection(self, stop_descriptions):
        # Display the next stops and allow the user to select one
        selected_stop = simpledialog.askstring("Select Next Stop", stop_descriptions)
        return selected_stop

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
