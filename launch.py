#! /usr/bin/evn python

import Tkinter

def tkexit():
  """
  Closes all the screens and exits the program
  """
  exit()

def mmenu():
  """
  main menu
  """
  results=Tkinter.Label(text="\nKUROBOT\nv0.0.0\n\n\n\n")
  #results.grid(row=1, column=1)
  results.pack()
  opt1button=Tkinter.Button(text="New Game",width=10)
  opt1button.pack()
  opt2button=Tkinter.Button(text="Continue",width=10)
  opt2button.pack()
  opt3button=Tkinter.Button(text="Options",width=10)
  opt3button.pack()
  opt4button=Tkinter.Button(text="Exit",width=10,command=tkexit)
  opt4button.pack()
    
if __name__=="__main__":
  root = Tkinter.Tk()
  root.wm_title("Kurobot dev")
  mmenu()

  Tkinter.mainloop()
