import tkinter as tk
from Globals import Globals
from Game import Game
from Point import Point


class Drawer():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("440x440")
        self.game = Game()
        self.canvas = tk.Canvas()
        self.draw()
        
        self.root.bind('<Button-1>', self.kill_snake)
        
        self.root.mainloop()


    def kill_snake(self, event):
        x = event.x // Globals.field_size - 1
        y = event.y // Globals.field_size - 1
        i = 0
        while i < len(self.game.snakes):
            if self.game.snakes[i].coordinates[0] == Point(x, y):
                del self.game.snakes[i]
                self.game.score += 100
                if len(self.game.snakes) == 0:
                    print(f"YOU WON! YOUR SCORE: {self.game.score}")
                    exit()
            else:
                i += 1


    def draw(self):
        self.game.run()
        self.canvas.delete("all")
        for i in range(1, 21):
            for j in range(1, 21):
                self.canvas.create_rectangle(i*Globals.field_size, 
                                        j*Globals.field_size, 
                                        i*Globals.field_size+20, 
                                        j*Globals.field_size+20, 
                                        fill="white", 
                                        outline="black")
        for snake in self.game.snakes:
            for coord in snake.coordinates:
                self.canvas.create_rectangle((coord.x+1)*Globals.field_size, 
                                        (coord.y+1)*Globals.field_size, 
                                        (coord.x+1)*Globals.field_size+20, 
                                        (coord.y+1)*Globals.field_size+20, 
                                        fill="blue", 
                                        outline="black")
            coord = snake.coordinates[0]
            self.canvas.create_rectangle((coord.x+1)*Globals.field_size, 
                                    (coord.y+1)*Globals.field_size, 
                                    (coord.x+1)*Globals.field_size+20, 
                                    (coord.y+1)*Globals.field_size+20, 
                                    fill="green", 
                                    outline="black")
        for fruit in self.game.fruits:
            coord = fruit.coordinates
            self.canvas.create_rectangle((coord.x+1)*Globals.field_size, 
                                    (coord.y+1)*Globals.field_size, 
                                    (coord.x+1)*Globals.field_size+20, 
                                    (coord.y+1)*Globals.field_size+20, 
                                    fill=fruit.color, 
                                    outline="black")
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.root.after(100, self.draw)
