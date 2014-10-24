#! /usr/bin/evn python

import Tkinter

def mmenu():
  """
  main menu
  """
  opt1button=Tkinter.Button(text="option 1")
  opt1button.pack()
  opt2button=Tkinter.Button(text="option 2")
  opt2button.pack()
    
if __name__=="__main__":
  root = Tkinter.Tk()
  root.wm_title("Kurobot dev")
  mmenu()

  Tkinter.mainloop()