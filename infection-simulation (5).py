import tkinter as tk
import tkinter.ttk as ttk
import time
import random
import sys
n = 100

class Person(object):
    # Constructor: creates a new person/agent
    def __init__(self, canvas, x, y, fill):
        # Calculate parameters for the oval/circle to be drawn
        r = 4 
        x0 = x-r
        y0 = y-r
        x1 = x+r
        y1 = y+r

        # Initialize the agents attributrs
        self.x = x
        self.y = y
        self.infected = False
        self.immune = False
        self.infected_time = 10

        self.canvas = canvas
        self.id = canvas.create_oval(x0,y0,x1,y1, fill=fill, outline='')

    #bevægelses mønster 
    def move(self):
        x1, y1, x2, y2 = self.canvas.bbox(self.id)
        dx = random.choice([-4, 4])
        dy = random.choice([-4, 4])


        self.canvas.move(self.id, dx, dy)
        self.x = self.x + dx 
        self.y = self.y + dy 

    def infected_time(self):
        z = self.infected_time = 5
        

    #smittet
    def check_infected(self, persons):
        for person in persons:
            d = ((self.x - person.x)**2 + (self.y - person.y)**2)**(1/2)

            if d < 20 and person.infected == True:
                self.infect()
                

        self.infected_time - 2 
        
    

    def check_immune(self):
        if self.infected_time == 0:
            self.infected = False
            self.immune = True 
              


    def infect(self):
        if self.immune == False: 
         self.infected = True
         self.canvas.itemconfig(self.id, fill='red')

    def immune(self):
        self.immune = True
        self.canvas.itemconfig(self.id, fill='green')





class App(object):
    def __init__(self, master, **kwargs):

        # Create the canvas on which the agents are drawn
        self.master = master
        self.canvas = tk.Canvas(self.master, width=800, height=800,background='white')
        self.canvas.pack()

        # Create a reset button for the simulation
        self.but_reset = ttk.Button(master, text = "Reset", command=self.init_sim)
        self.but_reset.pack(side=tk.BOTTOM)

        # Start / init the simulation
        self.init_sim()

        self.master.after(0, self.update)
        self.frame=0

    def update(self):

        # Update / move each agent
        for person in self.persons:
            person.move()
            person.check_infected(self.persons)
            person.check_immune()
            


        # Count number of infected persons
        ni = 0
        for p in self.persons:
            if p.infected:
                ni += 1
        print("Number of infected persons:", ni)


        # Count number of immune persons
        im = 0
        for i in self.persons:
            if i.immune:
                im += 1
        print("Number of immune persons:", im)



        self.master.after(100, self.update)
        self.frame += 1


    # Start / init simulation (clear all agents and create new ones)
    def init_sim(self):
        self.canvas.delete('all')
        self.persons = []

        for i in range(n):
            x = random.randint(0,800)
            y = random.randint(0,800)
            p = Person(self.canvas, x, y, 'black')
            if random.uniform(0,1) < 0.05:
                p.infect()

            self.persons.append(p)

        self.canvas.pack()

        
# Create the Tkinter application and run it
root = tk.Tk()
app = App(root)
start=time.time()
root.mainloop()
end=time.time()
print("Frames:",app.frame)
print("Runtime:",end-start)
print("Framerate:", app.frame/(end-start))

