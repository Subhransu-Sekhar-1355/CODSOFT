import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List")
        self.root.geometry("420x580")
        self.root.config(bg="#f0f2f5")
        self.tasks = []

        # Title
        tk.Label(root, text="To-Do List", font=("Arial", 24, "bold"), bg="#f0f2f5", fg="#333").pack(pady=15)

        # Input Frame
        self.input_frame = tk.Frame(root, bg="#f0f2f5")
        self.input_frame.pack(pady=5)

        self.task_entry = tk.Entry(self.input_frame, width=26, font=("Arial", 14))
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.add_btn = tk.Button(self.input_frame, text="Add Task", font=("Arial", 12), command=self.add_task, bg="#4CAF50", fg="white")
        self.add_btn.pack(side=tk.LEFT, padx=5)

        # Search Frame
        self.search_frame = tk.Frame(root, bg="#f0f2f5")
        self.search_frame.pack(pady=5)

        self.search_entry = tk.Entry(self.search_frame, width=30, font=("Arial", 12))
        self.search_entry.pack(side=tk.LEFT, padx=(10, 5))
        self.search_btn = tk.Button(self.search_frame, text="Search", command=self.search_task)
        self.search_btn.pack(side=tk.LEFT)

        # Task Listbox
        self.listbox = tk.Listbox(root, width=45, height=16, font=("Arial", 13), selectbackground="#c0c0c0")
        self.listbox.pack(pady=15)

        # Buttons Frame
        self.btn_frame = tk.Frame(root, bg="#f0f2f5")
        self.btn_frame.pack(pady=10)

        tk.Button(self.btn_frame, text="Mark Done", width=12, command=self.mark_done, bg="#2196F3", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(self.btn_frame, text="Delete", width=12, command=self.delete_task, bg="#f44336", fg="white").grid(row=0, column=1, padx=5)
        tk.Button(self.btn_frame, text="Clear All", width=12, command=self.clear_all, bg="#9C27B0", fg="white").grid(row=0, column=2, padx=5)

        # Empty Message
        self.empty_label = tk.Label(root, text="No tasks yet! Add some above.", font=("Arial", 11), fg="gray", bg="#f0f2f5")
        self.empty_label.pack()

        self.update_empty_state()

    def update_empty_state(self):
        if self.listbox.size() == 0:
            self.empty_label.config(text="No tasks yet! Add some above.")
        else:
            self.empty_label.config(text="")

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            timestamp = datetime.now().strftime(" [%I:%M %p]")
            full_task = task + timestamp
            self.tasks.append(full_task)
            self.listbox.insert(tk.END, full_task)
            self.task_entry.delete(0, tk.END)
            self.update_empty_state()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.listbox.delete(index)
            self.tasks.pop(index)
            self.update_empty_state()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            text = self.listbox.get(index)
            if text.startswith("✔ "):
                # Unmark
                original = text[2:]
                self.listbox.delete(index)
                self.listbox.insert(index, original)
            else:
                # Mark done
                self.listbox.delete(index)
                self.listbox.insert(index, "✔ " + text)
                self.listbox.itemconfig(index, {'fg': 'gray'})
        else:
            messagebox.showwarning("Selection Error", "Please select a task.")

    def clear_all(self):
        confirm = messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?")
        if confirm:
            self.listbox.delete(0, tk.END)
            self.tasks.clear()
            self.update_empty_state()

    def search_task(self):
        query = self.search_entry.get().strip().lower()
        self.listbox.delete(0, tk.END)
        filtered = [task for task in self.tasks if query in task.lower()]
        for task in filtered:
            self.listbox.insert(tk.END, task)
        if not filtered:
            self.listbox.insert(tk.END, "No matching tasks found.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
