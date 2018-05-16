###########################################################################################
# Name: Joshua S., Katherine G.
# Date: Time is Relative
# Description: DEAL OR NO DEAL - A game to dangle normally unachievable amounts of
#                 money in front of normal, desperate people. It's kind of sick.
###########################################################################################
from Tkinter import *
# from RPi.GPIO import GPIO
from random import randint
from time import *
from math import sqrt

PRIZE_VALS = [1, 5, 10, 25, 50, 100, 250, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 250000, 500000, 750000, 1000000]
YOUR_CASE = ""
OpenCases = 0
enabledVals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
disabledVals = []

# GUI setup
class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white")
        self.setupGUI()

    def setupGUI(self, version=0):
        if (version == 0):
            self.display = Label(self, text ="Pick your case!", bg ="white", height = 2, width = 15,\
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
            img = PhotoImage(file = "images/1.gif")
            self.b1 = Button(self, bg = "white", image = img, borderwidth = 0,\
                            highlightthickness = 0, activebackground = "white",\
                            command=lambda:self.process(str (MainGUI.assign(self, 1))))
            # set image
            self.b1.image = img
            # put button in place
            self.b1.grid(row = 1, column = 0, sticky = N+S+E+W)

           # case 2
            img = PhotoImage(file = "images/2.gif")
            self.b2 = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command=lambda: self.process(str (MainGUI.assign(self, 2))))
            # set image
            self.b2.image = img
            # put button in place
            self.b2.grid(row = 1, column = 1, sticky = N+S+E+W)

           # case 3
            img = PhotoImage(file = "images/3.gif")
            self.b3 = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command=lambda: self.process(str (MainGUI.assign(self, 3))))
            # set image
            self.b3.image = img
            # put button in place
            self. b3.grid(row = 1, column = 2, sticky = N+S+E+W)

           # case 4
            img = PhotoImage(file = "images/4.gif")
            self.b4 = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command=lambda: self.process(str (MainGUI.assign(self, 4))))
            # set image
            self.b4.image = img
            # put button in place
            self.b4.grid(row = 1, column = 3, sticky = N+S+E+W)

            ########################################################################
            # second row
            # case 5
            img = PhotoImage(file = "images/5.gif")
            self.b5 = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command=lambda: self.process(str (MainGUI.assign(self, 5))))
            # set image
            self.b5.image = img
            # put button in place
            self.b5.grid(row = 2, column = 0, sticky = N+S+E+W)

            # case 6
            img = PhotoImage(file = "images/6.gif")
            self.b6 = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command=lambda: self.process(str (MainGUI.assign(self, 6))))
            # set image
            self.b6.image = img
            # put button in place
            self.b6.grid(row = 2, column = 1, sticky = N+S+E+W)

            # case 7
            img = PhotoImage(file = "images/7.gif")
            self.b7 = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command=lambda: self.process(str (MainGUI.assign(self, 7))))
            # set image
            self.b7.image = img
            # put button in place
            self.b7.grid(row = 2, column = 2, sticky = N+S+E+W)

            # case 8
            img = PhotoImage(file = "images/8.gif")
            self.b8 = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command=lambda: self.process(str (MainGUI.assign(self, 8))))
            # set image
            self.b8.image = img
            # put button in place
            self.b8.grid(row = 2, column = 3, sticky = N+S+E+W)

            #######################################################################
            # third row
            # case 9
            img = PhotoImage(file = "images/9.gif")
            self.b9 = Button(self, bg = "white", image = img, borderwidth = 0,\
                        highlightthickness = 0, activebackground = "white",\
                        command=lambda: self.process(str (MainGUI.assign(self, 9))))
            # set image
            self.b9.image = img
            # put button in place
            self.b9.grid(row = 3, column = 0, sticky = N+S+E+W)

            # case 10
            img = PhotoImage(file = "images/10.gif")
            self.b10 = Button(self, bg = "white", image = img, borderwidth = 0,\
                         highlightthickness = 0, activebackground = "white",\
                         command=lambda: self.process(str (MainGUI.assign(self, 10))))
            # set image
            self.b10.image = img
            # put button in place
            self.b10.grid(row = 3, column = 1, sticky = N+S+E+W)

            # case 11
            img = PhotoImage(file = "images/11.gif")
            self.b11 = Button(self, bg = "white", image = img, borderwidth = 0,\
                         highlightthickness = 0, activebackground = "white",\
                         command=lambda: self.process(str (MainGUI.assign(self, 11))))
            # set image
            self.b11.image = img
            # put button in place
            self.b11.grid(row = 3, column = 2, sticky = N+S+E+W)

            # case 12
            img = PhotoImage(file = "images/12.gif")
            self.b12 = Button(self, bg = "white", image = img, borderwidth = 0,\
                         highlightthickness = 0, activebackground = "white",\
                         command=lambda: self.process(str (MainGUI.assign(self, 12))))
            # set image
            self.b12.image = img
            # put button in place
            self.b12.grid(row = 3, column = 3, sticky = N+S+E+W)

            ########################################################################
            # fourth row
            # case 13
            img = PhotoImage(file = "images/13.gif")
            self.b13 = Button(self, bg = "white", image = img, borderwidth = 0,\
                         highlightthickness = 0, activebackground = "white",\
                         command=lambda: self.process(str (MainGUI.assign(self, 13))))
            # set image
            self.b13.image = img
            # put button in place
            self.b13.grid(row = 4, column = 0, sticky = N+S+E+W)

            # case 14
            img = PhotoImage(file = "images/14.gif")
            self.b14 = Button(self, bg = "white", image = img, borderwidth = 0,\
                         highlightthickness = 0, activebackground = "white",\
                         command=lambda: self.process(str (MainGUI.assign(self, 14))))
            # set image
            self.b14.image = img
            # put button in place
            self.b14.grid(row = 4, column = 1, sticky = N+S+E+W)

            # case 15
            img = PhotoImage(file = "images/15.gif")
            self.b15 = Button(self, bg = "white", image = img, borderwidth = 0,\
                         highlightthickness = 0, activebackground = "white",\
                         command=lambda: self.process(str (MainGUI.assign(self, 15))))
            # set image
            self.b15.image = img
            # put button in place
            self.b15.grid(row = 4, column = 2, sticky = N+S+E+W)

            # case 16
            img = PhotoImage(file = "images/16.gif")
            self.b16 = Button(self, bg = "white", image = img, borderwidth = 0,\
                         highlightthickness = 0, activebackground = "white",\
                         command=lambda: self.process(str (MainGUI.assign(self, 16))))
            # set image
            self.b16.image = img
            # put button in place
            self.b16.grid(row = 4, column = 3, sticky = N+S+E+W)

            ########################################################################
            # fith row
            # case 17
            img = PhotoImage(file = "images/17.gif")
            self.b17 = Button(self, bg = "white", image = img, borderwidth = 0,\
                         highlightthickness = 0, activebackground = "white",\
                         command=lambda: self.process(str (MainGUI.assign(self, 17))))
            # set image
            self.b17.image = img
            # put button in place
            self.b17.grid(row = 5, column = 0, sticky = N+S+E+W)

            # case 18
            img = PhotoImage(file = "images/18.gif")
            self.b18 = Button(self, bg = "white", image = img, borderwidth = 0,\
                         highlightthickness = 0, activebackground = "white",\
                         command=lambda: self.process(str (MainGUI.assign(self, 18))))
            # set image
            self.b18.image = img
            # put button in place
            self.b18.grid(row = 5, column = 1, sticky = N+S+E+W)

            # case 19
            img = PhotoImage(file = "images/19.gif")
            self.b19 = Button(self, bg = "white", image = img, borderwidth = 0,\
                         highlightthickness = 0, activebackground = "white",\
                         command=lambda: self.process(str (MainGUI.assign(self, 19))))
            # set image
            self.b19.image = img
            # put button in place
            self.b19.grid(row = 5, column = 2, sticky = N+S+E+W)

            # case 20
            img = PhotoImage(file = "images/20.gif")
            self.b20 = Button(self, bg = "white", image = img, borderwidth = 0,\
                         highlightthickness = 0, activebackground = "white",\
                         command=lambda: self.process(str (MainGUI.assign(self, 20))))
            # set image
            self.b20.image = img
            # put button in place
            self.b20.grid(row = 5, column = 3, sticky = N+S+E+W)

            # pack the GUI
            self.pack(fill = BOTH, expand = 1)

            
        elif (version == 1):
            
            self.display = Label(self, text ="", bg ="white", height = 2, width = 15,\
                                 font = ("TextGyreAdventor", 50))
            self.display.grid(row = 0, column = 0, columnspan =4, sticky = E+W+N+S)

            # BAD BUTTON 1
            img = PhotoImage(file = "images/1.gif")
            self.b1 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b1.image = img
            # put button in place
            self.b1.grid(row = 1, column = 0, sticky = N+S+E+W)

            # BAD BUTTON 2
            # get rid of button 2
            img = PhotoImage(file = "images/2.gif")
            self.b2 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b2.image = img
            # put button in place
            self.b2.grid(row = 1, column = 1, sticky = N+S+E+W)

            # BAD BUTTON 3
            img = PhotoImage(file = "images/3.gif")
            self.b3 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b3.image = img
            # put button in place
            self.b3.grid(row = 1, column = 2, sticky = N+S+E+W)

            # BAD BUTTON 4
            img = PhotoImage(file = "images/4.gif")
            self.b4 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b4.image = img
            # put button in place
            self.b4.grid(row = 1, column = 3, sticky = N+S+E+W)

            # BAD BUTTON 5
            img = PhotoImage(file = "images/5.gif")
            self.b5 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b5.image = img
            # put button in place
            self.b5.grid(row = 2, column = 0, sticky = N+S+E+W)
            
            ############### Deal button #####################
            img = PhotoImage(file = "images/deal.gif")
            self.bdeal = Button(self, bg = "white", image = img, borderwidth = 0,\
                                highlightthickness = 0, activebackground = "white",\
                                command=lambda: MainGUI.DealNoDeal(self, 1))
            self.bdeal.image = img
            self.bdeal.grid(row = 2, column = 1, sticky = N+S+E+W)

            ############### No Deal button ###################
            img = PhotoImage(file = "images/nodeal.gif")
            self.bdeal = Button(self, bg = "white", image = img, borderwidth = 0,\
                                highlightthickness = 0, activebackground = "white",\
                                command=lambda: MainGUI.DealNoDeal(self, 2))
            self.bdeal.image = img
            self.bdeal.grid(row = 2, column = 2, sticky = N+S+E+W)

            # BAD BUTTON 8
            img = PhotoImage(file = "images/8.gif")
            self.b8 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b8.image = img
            # put button in place
            self.b8.grid(row = 2, column = 3, sticky = N+S+E+W)

            # BAD BUTTON 9
            img = PhotoImage(file = "images/9.gif")
            self.b9 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b9.image = img
            # put button in place
            self.b9.grid(row = 3, column = 0, sticky = N+S+E+W)

            # BAD BUTTON 10
            img = PhotoImage(file = "images/10.gif")
            self.b10 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b10.image = img
            # put button in place
            self.b10.grid(row = 3, column = 1, sticky = N+S+E+W)

            # BAD BUTTON 11
            img = PhotoImage(file = "images/11.gif")
            self.b11 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b11.image = img
            # put button in place
            self.b11.grid(row = 3, column = 2, sticky = N+S+E+W)

            # BAD BUTTON 12
            img = PhotoImage(file = "images/12.gif")
            self.b12 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b12.image = img
            # put button in place
            self.b12.grid(row = 3, column = 3, sticky = N+S+E+W)

            # BAD BUTTON 13
            img = PhotoImage(file = "images/13.gif")
            self.b13 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b13.image = img
            # put button in place
            self.b13.grid(row = 4, column = 0, sticky = N+S+E+W)

            # BAD BUTTON 14
            img = PhotoImage(file = "images/14.gif")
            self.b14 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b14.image = img
            # put button in place
            self.b14.grid(row = 4, column = 1, sticky = N+S+E+W)

            # BAD BUTTON 15
            img = PhotoImage(file = "images/15.gif")
            self.b15 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b15.image = img
            # put button in place
            self.b15.grid(row = 4, column = 2, sticky = N+S+E+W)

            # BAD BUTTON 16
            img = PhotoImage(file = "images/16.gif")
            self.b16 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b16.image = img
            # put button in place
            self.b16.grid(row = 4, column = 3, sticky = N+S+E+W)

            # BAD BUTTON 17
            img = PhotoImage(file = "images/17.gif")
            self.b17 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b17.image = img
            # put button in place
            self.b17.grid(row = 5, column = 0, sticky = N+S+E+W)

            # BAD BUTTON 18
            img = PhotoImage(file = "images/18.gif")
            self.b18 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b18.image = img
            # put button in place
            self.b18.grid(row = 5, column = 1, sticky = N+S+E+W)

            # BAD BUTTON 19
            img = PhotoImage(file = "images/19.gif")
            self.b19 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b19.image = img
            # put button in place
            self.b19.grid(row = 5, column = 2, sticky = N+S+E+W)

            # BAD BUTTON 20
            img = PhotoImage(file = "images/20.gif")
            self.b20 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b20.image = img
            # put button in place
            self.b20.grid(row = 5, column = 3, sticky = N+S+E+W)
            
            self.pack(fill = BOTH, expand = 1)
            


    def assign(self, num):
        global disabledVals
        i = randint(0, len(PRIZE_VALS)- 1)
        value = PRIZE_VALS[i]
        MainGUI.negate(self, num)
        disabledVals.append(num)
        del PRIZE_VALS[i]
        return value

    def negate(self, num):
        if (num == 1):
            # get rid of button 1
            img = PhotoImage(file = "images/1.gif")
            self.b1 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b1.image = img
            # put button in place
            self.b1.grid(row = 1, column = 0, sticky = N+S+E+W)

        elif (num == 2):
            # get rid of button 2
            img = PhotoImage(file = "images/2.gif")
            self.b2 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b2.image = img
            # put button in place
            self.b2.grid(row = 1, column = 1, sticky = N+S+E+W)

        elif (num == 3):
            img = PhotoImage(file = "images/3.gif")
            self.b3 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b3.image = img
            # put button in place
            self.b3.grid(row = 1, column = 2, sticky = N+S+E+W)

        elif (num == 4):
            img = PhotoImage(file = "images/4.gif")
            self.b4 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b4.image = img
            # put button in place
            self.b4.grid(row = 1, column = 3, sticky = N+S+E+W)

        elif (num == 5):
            img = PhotoImage(file = "images/5.gif")
            self.b5 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b5.image = img
            # put button in place
            self.b5.grid(row = 2, column = 0, sticky = N+S+E+W)

        elif (num == 6):
            img = PhotoImage(file = "images/6.gif")
            self.b6 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b6.image = img
            # put button in place
            self.b6.grid(row = 2, column = 1, sticky = N+S+E+W)

        elif (num == 7):
            img = PhotoImage(file = "images/7.gif")
            self.b7 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b7.image = img
            # put button in place
            self.b7.grid(row = 2, column = 2, sticky = N+S+E+W)

        elif (num == 8):
            img = PhotoImage(file = "images/8.gif")
            self.b8 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b8.image = img
            # put button in place
            self.b8.grid(row = 2, column = 3, sticky = N+S+E+W)

        elif (num == 9):
            img = PhotoImage(file = "images/9.gif")
            self.b9 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b9.image = img
            # put button in place
            self.b9.grid(row = 3, column = 0, sticky = N+S+E+W)

        elif (num == 10):
            img = PhotoImage(file = "images/10.gif")
            self.b10 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b10.image = img
            # put button in place
            self.b10.grid(row = 3, column = 1, sticky = N+S+E+W)

        elif (num == 11):
            img = PhotoImage(file = "images/11.gif")
            self.b11 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b11.image = img
            # put button in place
            self.b11.grid(row = 3, column = 2, sticky = N+S+E+W)

        elif (num == 12):
            img = PhotoImage(file = "images/12.gif")
            self.b12 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b12.image = img
            # put button in place
            self.b12.grid(row = 3, column = 3, sticky = N+S+E+W)

        elif (num == 13):
            img = PhotoImage(file = "images/13.gif")
            self.b13 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b13.image = img
            # put button in place
            self.b13.grid(row = 4, column = 0, sticky = N+S+E+W)

        elif (num == 14):
            img = PhotoImage(file = "images/14.gif")
            self.b14 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b14.image = img
            # put button in place
            self.b14.grid(row = 4, column = 1, sticky = N+S+E+W)

        elif (num == 15):
            img = PhotoImage(file = "images/15.gif")
            self.b15 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b15.image = img
            # put button in place
            self.b15.grid(row = 4, column = 2, sticky = N+S+E+W)

        elif (num == 16):
            img = PhotoImage(file = "images/16.gif")
            self.b16 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b16.image = img
            # put button in place
            self.b16.grid(row = 4, column = 3, sticky = N+S+E+W)

        elif (num == 17):
            img = PhotoImage(file = "images/17.gif")
            self.b17 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b17.image = img
            # put button in place
            self.b17.grid(row = 5, column = 0, sticky = N+S+E+W)

        elif (num == 18):
            img = PhotoImage(file = "images/18.gif")
            self.b18 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b18.image = img
            # put button in place
            self.b18.grid(row = 5, column = 1, sticky = N+S+E+W)

        elif (num == 19):
            img = PhotoImage(file = "images/19.gif")
            self.b19 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b19.image = img
            # put button in place
            self.b19.grid(row = 5, column = 2, sticky = N+S+E+W)

        elif (num == 20):
            img = PhotoImage(file = "images/20.gif")
            self.b20 = Button(self, bg = "white", image = img, borderwidth = 0,\
                             highlightthickness = 0, activebackground = "white",\
                             state = "disabled")
            # set image
            self.b20.image = img
            # put button in place
            self.b20.grid(row = 5, column = 3, sticky = N+S+E+W)
        
            

    def process(self, button):
        global YOUR_CASE
        global OpenCases
        if (OpenCases > 0):
            self.display["text"] = ""
            self.display["text"] += button
            print button
            
            if (OpenCases == 5):
                MainGUI.setupGUI(self, 1)
                self.display["text"] = "{}\nOffer: ${}" .format(button, MainGUI.Bank_offer(self))
                
            elif (OpenCases == 9):
                MainGUI.setupGUI(self, 1)
                self.display["text"] = "{}\nOffer: ${}" .format(button, MainGUI.Bank_offer(self))
                
            elif (OpenCases == 12):
                MainGUI.setupGUI(self, 1)
                self.display["text"] = "{}\nOffer: ${}" .format(button, MainGUI.Bank_offer(self))
                
            elif (OpenCases == 15):
                MainGUI.setupGUI(self, 1)
                self.display["text"] = "{}\nOffer: ${}" .format(button, MainGUI.Bank_offer(self))

            elif (OpenCases == 17):
                MainGUI.setupGUI(self, 1)
                self.display["text"] = "{}\nOffer: ${}" .format(button, MainGUI.Bank_offer(self))

            elif (OpenCases == 19):
                self.display["text"] = "Your case was:\n${}" .format(YOUR_CASE)

        elif (OpenCases == 0):
            YOUR_CASE = button
            print YOUR_CASE

        OpenCases += 1

    def Bank_offer(self):
        offer = 0
        for i in range(len(PRIZE_VALS) - 1):
            offer += (PRIZE_VALS[i]) ** 2
        offer = sqrt(offer / (len(PRIZE_VALS))) 
        return str(round(offer, 2))

    def DealNoDeal(self, button):
        if (button == 1):
            print PRIZE_VALS
            self.display["text"] = "Won ${}!\nCongratulations!" .format(MainGUI.Bank_offer(self))
        elif (button == 2):
            MainGUI.setupGUI(self, 0)
            self.display["text"] = "Keep going!"
            for i in disabledVals:
                MainGUI.negate(self, i)
            

################################################################################
window = Tk()
# window title
window.title("Deal or No Deal")
# generate the GUI
p = MainGUI(window)
# display the GUI and wait for user interaction
window.mainloop()
