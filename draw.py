import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digit Drawing App")
        
        self.canvas = tk.Canvas(self.root, width=700, height=700, bg='white')
        self.canvas.pack()
        
        self.button_save = ttk.Button(self.root, text="Save", command=self.save_drawing)
        self.button_save.pack(side=tk.LEFT)
        
        self.button_clear = ttk.Button(self.root, text="Clear", command=self.clear_drawing)
        self.button_clear.pack(side=tk.LEFT)
        
        self.button_exit = ttk.Button(self.root, text="Exit", command=self.root.quit)
        self.button_exit.pack(side=tk.LEFT)
        
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)
        
        self.drawing = False
        self.last_x, self.last_y = 0, 0
        self.image = Image.new("L", (700, 700), 0)
        self.draw = ImageDraw.Draw(self.image)

    def start_drawing(self, event):
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.drawing:
            x, y = event.x, event.y
            self.canvas.create_rectangle((self.last_x, self.last_y, x, y), fill="black", width=50)
            self.draw.line((self.last_x, self.last_y, x, y), fill=200, width=50)
            self.last_x, self.last_y = x, y

    def stop_drawing(self, event):
        self.drawing = False

    def save_drawing(self):
        filename = "drawn_digit.png"
        self.image.save(filename)
        print(f"Saved {filename}")

    def clear_drawing(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (700, 700), 0)
        self.draw = ImageDraw.Draw(self.image)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
