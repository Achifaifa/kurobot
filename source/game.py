#! /usr/bin/env python

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
  gamemenu.add_command(label="Options")
  gamemenu.add_separator()
  gamemenu.add_command(label="Exit",command=exitwin)
  #Team management drop down menu
  teammenu=Tkinter.Menu(menubar, tearoff=0)
  teammenu.add_command(label="Manage")
  teammenu.add_command(label="Members")
  teammenu.add_command(label="Train")
  teammenu.add_command(label="Info")
  #Robot management drop down menu
  robotmenu=Tkinter.Menu(menubar, tearoff=0)
  robotmenu.add_command(label="Status")
  robotmenu.add_command(label="components")
  robotmenu.add_command(label="Upgrades")
  robotmenu.add_command(label="Repair")
  #Finances drop down menu
  financesmenu=Tkinter.Menu(menubar, tearoff=0)
  financesmenu.add_command(label="Bank")
  financesmenu.add_command(label="Sponsors")
  financesmenu.add_command(label="Expenses")
  #Menu integration
  menubar.add_cascade(menu=gamemenu, label="Game")
  menubar.add_cascade(menu=teammenu, label="Team")
  menubar.add_cascade(menu=robotmenu, label="Robot")
  menubar.add_cascade(menu=financesmenu, label="Finances")
  print "OK"
  Tkinter.mainloop()

def exitwin():
  """
  Closes the game window and returns to the main menu
  """

  pass

if __name__=="__main__": 

  print "Game window and main procedures module"
  print "Testing... ",
  print "[testing disabled]"
  exit()
