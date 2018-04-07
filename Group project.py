#################################################################################
# Name: Joshua S.
# Date:
# Description:
################################################################################
from Tkinter import *

# GUI setup
class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white")
        self.setupGUI()

    def setupGUI(self):
        self.display = Label(self, text ="", bg ="white", height = 2, width = 15,\
                             font = ("TextGyreAdventor", 50))
        self.display.grid(row = 0, column = 0, columnspan =4, sticky = E+W+N+S)

        # layout(still need images)
        # 1 2 3 4
        # 5 6 7 8
        # 9 10 11 12
        # 13 14 15 16
        # 17 18 19 20

        # first row
        # 1
        img = PhotoImage(file = )# needs images
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 1, column = 0, sticky = N+S+E+W)
        # pack the GUI
        self.pack(fill = BOTH, expand = 1)

############################
window = Tk()
# window title
window.title("Deal or No Deal")
# generate the GUI
p = MainGUI(window)
# display the GUI and wait for user interaction
window.mainloop()
