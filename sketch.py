import tkinter as tk
import math


class Sketch:
    def __init__(self, root):
        self.root = root

        self.root.title("PySketch")
        self.root.geometry("1000x1000")
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=1)

        self.center = [500, 1000]
        self.distance = 1
        self.points = []
        self.angles = []
        self.distances = []
        self.xangle = (math.pi / 2)
        self.width = 6
        self.angle = (math.pi / 6)
        self.n = 1
        self.lsystem = "F"
        self.canvas.bind("<Button-1>", lambda x: self.generate_lsystem(self.lsystem))
        self.canvas.config(bg="#242424")
        self.root.update()


        self.root.mainloop()

    def get_point(self, start_point, distance):
        return [start_point[0] + (distance * math.cos(self.xangle)), start_point[1] + (distance * -math.sin(self.xangle))]

    def generate_lsystem(self, string):
        self.lsystem = string.replace("F", "FF+[+F-F-F]-[-F+F+F]")
        self.reset()
        self.n +=1
        self.width -= 1
        for x in self.lsystem:
            if x == "F":
                xc, yc = self.get_point(self.center, self.distance)
                self.canvas.create_line(self.center[0], self.center[1], xc, yc, width=self.width, capstyle=tk.ROUND, fill="white")
                self.center = [xc, yc]
            elif x == "+":
                self.xangle -= self.angle
            elif x == "-":
                self.xangle += self.angle
            elif x == "[":
                self.points.append(self.center)
                self.angles.append(self.xangle)
                self.distances.append(self.distance)
            elif x == "]":
                self.center = self.points[-1]
                self.points = self.points[:-1]
                self.xangle = self.angles[-1]
                self.angles = self.angles[:-1]
                self.distance = self.distances[-1]
                self.distances = self.distances[:-1]

    def reset(self):
        self.center = [500, 1000]
        self.distance = 10/(self.n*0.25)
        self.points = []
        self.angles = []
        self.distances = []
        self.xangle = (math.pi / 2)



if __name__ == "__main__":
    sketch = Sketch(tk.Tk())
