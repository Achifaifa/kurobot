#! /usr/bin/evn python

import Tkinter

elements=[] 
root=0

def loop():
  """
  Main game loop
  """

  makewin()

def makewin():
  """
  Initializes the game window and returns it.
  """

  #Create global game window
  print "Creating game screen... ",
  root=Tkinter.Tk()
  root.wm_title("Kurobot")
  #Create menu bar
  menubar=Tkinter.Menu(root)  
  root.config(menu=menubar)
  #Game drop down menu
  gamemenu=Tkinter.Menu(menubar, tearoff=0)
  gamemenu.add_command(label="Load")
  gamemenu.add_command(label="Save")
  gamemenu.add_separator()
  gamemenu.add_command(label="Exit")
  menubar.add_cascade(menu=gamemenu, label="Game")
  print "OK"
  Tkinter.mainloop()

if __name__=="__main__": pass
