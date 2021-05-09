import tkinter as tk
from Globals import Globals
from Field import Field
from Game import Game
from Point import Point


class Drawer():
    '''
    Facade pattern class for drawind and displaying all objects with Tkinter library
    '''

    def __init__(self):
        self.root = tk.Tk()
        self.square_width = 1
        self.game = Game()
        self.canvas = tk.Canvas()
        self.menu()
        self.label = tk.Label(text=f"Score: {self.game.score}")
        self.label.pack()
        self.root.bind('<Button-1>', self.kill_snake)
        self.root.mainloop()

    def menu(self):
        '''
        Displays main menu with buttons for choosing difficulty
        '''
        self.root.geometry("100x100+500+200")

        def but(x):
            self.game.choose_difficulty(x)
            if Field.field_size == 10:
                self.square_width = 40
                self.root.geometry(
                    f"{self.square_width*10+2*self.square_width}x{self.square_width*10+2*self.square_width}+200+200")
            elif Field.field_size == 20:
                self.square_width = 20
                self.root.geometry(
                    f"{self.square_width*20+2*self.square_width}x{self.square_width*20+2*self.square_width}+200+200")
            elif Field.field_size == 30:
                self.square_width = 20
                self.root.geometry(
                    f"{self.square_width*30+2*self.square_width}x{self.square_width*30+2*self.square_width}+300+1")
            b1.destroy()
            b2.destroy()
            b3.destroy()
            self.draw()

        b1 = tk.Button(text="Low",
                       command=lambda: but(1))
        b2 = tk.Button(text="Medium",
                       command=lambda: but(2))
        b3 = tk.Button(text="Insane",
                       command=lambda: but(3))
        b1.pack()
        b2.pack()
        b3.pack()

    def kill_snake(self, event):
        '''
        Button event handler. 
        If player clicks on Snakes head, it dies.
        '''
        x = event.x // self.square_width - 1
        y = event.y // self.square_width - 1
        i = 0
        while i < len(self.game.snakes):
            if self.game.snakes[i].coordinates[0] == Point(x, y):
                del self.game.snakes[i]
                self.game.score += self.game.difficulty*100
                if len(self.game.snakes) == 0:
                    print(f"YOU WON! YOUR SCORE: {self.game.score}")
                    exit()
            else:
                i += 1

    def draw(self):
        '''
        Main function that displays all objects in drawed field.
        '''
        self.game.run()
        self.canvas.delete("all")
        self.label.config(text=f"Score: {self.game.score}")
        for i in range(1, Field.field_size+1):
            for j in range(1, Field.field_size+1):
                self.canvas.create_rectangle(i*self.square_width,
                                             j*self.square_width,
                                             i*self.square_width+self.square_width,
                                             j*self.square_width+self.square_width,
                                             fill="white",
                                             outline="black")
        for snake in self.game.snakes:
            for coord in snake.coordinates:
                self.canvas.create_rectangle((coord.x+1)*self.square_width,
                                             (coord.y+1)*self.square_width,
                                             (coord.x+1)*self.square_width +
                                             self.square_width,
                                             (coord.y+1)*self.square_width +
                                             self.square_width,
                                             fill="blue",
                                             outline="black")
            coord = snake.coordinates[0]
            self.canvas.create_rectangle((coord.x+1)*self.square_width,
                                         (coord.y+1)*self.square_width,
                                         (coord.x+1)*self.square_width +
                                         self.square_width,
                                         (coord.y+1)*self.square_width +
                                         self.square_width,
                                         fill="green",
                                         outline="black")
        for fruit in self.game.fruits:
            coord = fruit.coordinates
            self.canvas.create_rectangle((coord.x+1)*self.square_width,
                                         (coord.y+1)*self.square_width,
                                         (coord.x+1)*self.square_width +
                                         self.square_width,
                                         (coord.y+1)*self.square_width +
                                         self.square_width,
                                         fill=fruit.color,
                                         outline="black")
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.root.after(Globals.display_delay, self.draw)
