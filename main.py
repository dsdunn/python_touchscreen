from tkinter import *
import tkinter.font
# from gpiozero import LED
# import RPi.GPIO
# RPi.GPIO.setmode(RPi.GPIO.BCM)


class CarControl:

  def __init__(self, master = None):
    self.master = master
    master.title('Car Control')

    self.start_button = Button(master, text="On", command=self.start)
    self.start_button.pack(side=LEFT)

    self.window_control = Frame(master, bd=5, bg="lightblue", width=300, height=200)
    self.window_control.pack()
    self.window_control.grid_propagate(0)

    self.button1 = Button(self.window_control, height=3, width=6,command= lambda: self.window_up("1"), text='1') 
    self.button1.grid(row=0, column=0)
    self.button1.rowconfigure(0, minsize=45)
    self.button1.columnconfigure(0, minsize=25)

    self.button2 = Button(self.window_control, command= lambda: self.window_down("1"), text='2') 
    self.button2.grid(row=1, column=0)

    self.button3 = Button(self.window_control, command= lambda: self.window_up("2"), text='3') 
    self.button3.grid(row=0, column=2)

    self.button4 = Button(self.window_control, command= lambda: self.window_down("2"), text='4') 
    self.button4.grid(row=1, column=2)

  def start(self):
    if self.start_button.config('text')[-1] == "On":
      self.start_button.config(text="Off")
      print("vrooom!")
    else:
      self.start_button.config(text= "On")
      print("poooffff")

  def window_up(self, num):
    print("up: " + num)

  def window_down(self, num):
    print("down: " + num)



root = Tk()
root.geometry("800x480")

app = CarControl(root)

root.mainloop()

