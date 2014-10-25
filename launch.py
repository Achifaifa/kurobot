#! /usr/bin/evn python

import Tkinter

def tkexit():
  """
  Closes all the screens and exits the program
  """
  exit()

def clsr():
  """
  Deletes all the elements in the screen 
  """
  global elements
  for i in elements: i.pack_forget()
  elements=[]

def mmenu():
  """
  main menu
  """

  clsr()
  title=Tkinter.Label(text="\nKUROBOT\nv0.0.0\n\n\n\n")
  title.pack()
  elements.append(title)
  opt1button=Tkinter.Button(text="New Game",width=10)
  opt1button.pack()
  elements.append(opt1button)
  opt2button=Tkinter.Button(text="Continue",width=10)
  opt2button.pack()
  elements.append(opt2button)
  opt3button=Tkinter.Button(text="Options",width=10,command=optionm)
  opt3button.pack()
  elements.append(opt3button)
  opt4button=Tkinter.Button(text="Exit",width=10,command=tkexit)
  opt4button.pack()
  elements.append(opt4button)

def optionm():
  """
  Options menu
  """

  clsr()
  title=Tkinter.Label(text="\nKUROBOT\nv0.0.0\n\n\n\n")
  title.pack()
  elements.append(title)
  opt1button=Tkinter.Button(text="Option1",width=10)
  opt1button.pack()
  elements.append(opt1button)
  opt2button=Tkinter.Button(text="Option2",width=10)
  opt2button.pack()
  elements.append(opt2button)
  opt3button=Tkinter.Button(text="Back",width=10,command=mmenu)
  opt3button.pack()
  elements.append(opt3button)


if __name__=="__main__":
  elements=[] 
  root = Tkinter.Tk()
  root.wm_title("Kurobot dev")
  mmenu()

  Tkinter.mainloop()
