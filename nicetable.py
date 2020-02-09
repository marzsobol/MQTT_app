import tkinter as tk
from PIL import ImageTk, Image
import math
import threading


class GUI(tk.Frame, threading.Thread):
    def __init__(self, parent, names_how_many_columns):
        tk.Frame.__init__(self, parent)
        parent.config(bg = "PaleVioletRed1")


        grid_size_width = math.trunc(800/(len(names_how_many_columns) + 1))
        grid_size_height = math.trunc(400/3)

        self.oking = Image.open("ok.png")
        self.oking = self.oking.resize((grid_size_height, grid_size_width), Image.ANTIALIAS)
        self.oking = ImageTk.PhotoImage(image=self.oking)

        self.nookimg = Image.open("nook.png")
        self.nookimg = self.nookimg.resize((grid_size_height, grid_size_width), Image.ANTIALIAS)
        self.nookimg = ImageTk.PhotoImage(image = self.nookimg)

        for row in range(3):
            parent.grid_rowconfigure(row, weight=1)
        for col in range(len(names_how_many_columns) + 1):
            parent.grid_columnconfigure(col, weight=1)


        self.welcoming = tk.Label(parent, text = "Which message was taken?", background="RosyBrown1")
        self.welcoming.grid(row=0, column=0, sticky="nsew", columnspan= len(names_how_many_columns) + 1, rowspan=1)

        column_name_group_start = 1
        row_name_group = 1
        self.labelsgroupname = []
        self.namegroup =tk.Label (parent, text= "Group: ", background="RosyBrown1")
        self.namegroup.grid(row = 1, column = 0, sticky = "nsew", columnspan = 1)

        for names in  (names_how_many_columns):
            self.labelsgroupname.append(tk.Label(parent, text=names, background="RosyBrown3"))
            # print(row_name_group, " na ", column_name_group_start )
            self.labelsgroupname[-1].grid(row = row_name_group, column = column_name_group_start, sticky="nsew",columnspan = 1, rowspan = 1)
            column_name_group_start = 1 + column_name_group_start

        self.accomplished = []
        column_name_group_start = 1
        row_name_group = 2
        for names in range (0,( len(names_how_many_columns))):
            self.accomplished.append(tk.Label(parent, image = self.nookimg, background="RosyBrown2"))
            self.accomplished[names].grid(row = row_name_group, column = column_name_group_start,columnspan = 1,  rowspan = 1, sticky = "nsew")
            column_name_group_start = 1 + column_name_group_start

    def change_status(self, which_group):
        print("table")
        self.accomplished[which_group].config(image=self.oking)





