#! /usr/bin/evn python

import game
import Tkinter

def tkexit():
  """
  Closes all the screens and exits the program
  """
  exit()

def menutitle():
  """
  Prints the menu title
  """

  title=Tkinter.Label(text="\nKUROBOT\nv0.0.0\n\n\n\n")
  elements.append(title)

def mmenu():
  """
  main menu
  """

  clsr()
  menutitle()
  opt1button=Tkinter.Button(text="New Game",width=10,command=game.loop)
  elements.append(opt1button)
  opt2button=Tkinter.Button(text="Continue",width=10,bg="#111111")
  elements.append(opt2button)
  opt3button=Tkinter.Button(text="Options",width=10,command=optionm)
  elements.append(opt3button)
  opt4button=Tkinter.Button(text="Exit",width=10,command=tkexit)
  elements.append(opt4button)
  packall()

def optionm():
  """
  Options menu
  """

  clsr()
  menutitle()
  opt1button=Tkinter.Button(text="Option1",width=10)
  elements.append(opt1button)
  opt2button=Tkinter.Button(text="Option2",width=10)
  elements.append(opt2button)
  opt3button=Tkinter.Button(text="Back",width=10,command=mmenu)
  elements.append(opt3button)
  packall()

def packall():
  """
  Packs all the elements in the elements list
  """

  global elements
  for i in elements: i.pack()

def gamewindow():
  """
  Sets up the game window
  """

  gamewin=Tkinter.Tk()
  gamewin.wm_title("Kurobot")
  gamewin.bind_all()
  gamewin.mainloop()

def clsr():
  """
  Deletes all the elements in the screen.

  Not for use on the main menus
  """

  global elements
  for i in elements: i.pack_forget()
  elements=[]

if __name__=="__main__":
  elements=[] 
  root=Tkinter.Tk()
  root.wm_title("Kurobot launcher [0.0.0]")
  mmenu()
  Tkinter.mainloop()
