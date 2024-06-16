import tkinter as tk
from tkinter import messagebox
import random
import string

class WordHuntingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Hunting Game")

        self.grid_size = 10
        self.grid = []
        self.word = ""
        self.score = 0
        self.time_left = 60  
        self.found_words = set()

        self.create_widgets()
        self.generate_grid()
        self.update_timer()

    def create_widgets(self):
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(pady=20)

        self.word_entry_label = tk.Label(self.root, text="Enter word to find:")
        self.word_entry_label.pack()
        self.word_entry = tk.Entry(self.root)
        self.word_entry.pack()

        self.find_button = tk.Button(self.root, text="Find Word", command=self.find_word)
        self.find_button.pack(pady=10)

        self.generate_grid_button = tk.Button(self.root, text="Generate New Grid", command=self.generate_grid)
        self.generate_grid_button.pack(pady=10)

        self.clear_highlight_button = tk.Button(self.root, text="Clear Highlights", command=self.clear_highlights)
        self.clear_highlight_button.pack(pady=10)

        self.score_label = tk.Label(self.root, text=f"Score: {self.score}")
        self.score_label.pack()

        self.timer_label = tk.Label(self.root, text=f"Time left: {self.time_left}s")
        self.timer_label.pack()

    def generate_grid(self):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        self.grid = []
        for row in range(self.grid_size):
            row_data = []
            for col in range(self.grid_size):
                char = random.choice(string.ascii_uppercase)
                row_data.append(char)
                label = tk.Label(self.grid_frame, text=char, width=2, height=1, borderwidth=1, relief="solid", font=("Helvetica", 16))
                label.grid(row=row, column=col, padx=2, pady=2)
            self.grid.append(row_data)
        self.clear_highlights()
        self.found_words.clear()

    def find_word(self):
        self.word = self.word_entry.get().upper()
        if not self.word:
            messagebox.showinfo("Input Error", "Please enter a word to find.")
            return
        if self.word in self.found_words:
            messagebox.showinfo("Duplicate Word", "You have already found this word.")
            return

        positions = self.search_word_in_grid()
        if positions:
            for pos in positions:
                row, col = pos
                self.grid_frame.grid_slaves(row=row, column=col)[0].config(bg="yellow")
            self.found_words.add(self.word)
            self.score += len(self.word)
            self.score_label.config(text=f"Score: {self.score}")
            messagebox.showinfo("Success", f"The word '{self.word}' was found!")
        else:
            messagebox.showinfo("Not Found", f"The word '{self.word}' was not found.")
        self.word_entry.delete(0, tk.END)

    def search_word_in_grid(self):
        word_len = len(self.word)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0),(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for r in range(self.grid_size):
            for c in range(self.grid_size):
                if self.grid[r][c] == self.word[0]:
                    for dr, dc in directions:
                        if all(
                            0 <= r + dr * i < self.grid_size and
                            0 <= c + dc * i < self.grid_size and
                            self.grid[r + dr * i][c + dc * i] == self.word[i]
                            for i in range(word_len)
                        ):
                            return [(r + dr * i, c + dc * i) for i in range(word_len)]
        return None

    def clear_highlights(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                self.grid_frame.grid_slaves(row=row, column=col)[0].config(bg="white")

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time's Up", f"Time's up! Your final score is {self.score}")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = WordHuntingGame(root)
    root.mainloop()
