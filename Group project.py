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
        # case 1
        img = PhotoImage(file = "images/1.gif")# possible image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 1, column = 0, sticky = N+S+E+W)

       # case 2
        img = PhotoImage(file = "images/2.gif")# possible image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 1, column = 1, sticky = N+S+E+W)

       # case 3
        img = PhotoImage(file = "images/3.gif")# possible image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 1, column = 2, sticky = N+S+E+W)

       # case 4
        img = PhotoImage(file = "images/4.gif")# possible image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 1, column = 3, sticky = N+S+E+W)

        ########################################################################
        # second row
        # case 5
        img = PhotoImage(file = "images/5.gif")# possible image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 2, column = 0, sticky = N+S+E+W)

        # case 6
        img = PhotoImage(file = "images/6.gif")# possible image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 2, column = 1, sticky = N+S+E+W)

        # case 7
        img = PhotoImage(file = "images/7.gif")# possible image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 2, column = 2, sticky = N+S+E+W)

        # case 8
        img = PhotoImage(file = "images/8.gif")# possible image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 2, column = 3, sticky = N+S+E+W)

        #######################################################################
        # third row
        # case 9
        img = PhotoImage(file = "images/9.gif")# possible image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 3, column = 0, sticky = N+S+E+W)

        # case 10
        img = PhotoImage(file = )# need image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 3, column = 1, sticky = N+S+E+W)

        # case 11
        img = PhotoImage(file = )# need image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 3, column = 2, sticky = N+S+E+W)

        # case 12
        img = PhotoImage(file = )# need image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 3, column = 3, sticky = N+S+E+W)

        ########################################################################
        # fourth row
        # case 13
        img = PhotoImage(file = )# need image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 4, column = 0, sticky = N+S+E+W)

        # case 14
        img = PhotoImage(file = )# need image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 4, column = 1, sticky = N+S+E+W)

        # case 15
        img = PhotoImage(file = )# need image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 4, column = 2, sticky = N+S+E+W)

        # case 16
        img = PhotoImage(file = )# need image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 4, column = 3, sticky = N+S+E+W)

        ########################################################################
        # fith row
        # case 17
        img = PhotoImage(file = )# need image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 5, column = 0, sticky = N+S+E+W)

        # case 18
        img = PhotoImage(file = )# need image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 5, column = 1, sticky = N+S+E+W)

        # case 19
        img = PhotoImage(file = )# need image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 5, column = 2, sticky = N+S+E+W)

        # case 20
        img = PhotoImage(file = )# need image
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white")
        # set image
        button.image = img
        # put button in place
        button.grid(row = 5, column = 3, sticky = N+S+E+W)

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
