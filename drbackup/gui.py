# encoding: utf-8
from Tkinter import *
import datetime 
from tkCommonDialog import Dialog

class Chooser(Dialog):

    command = "tk_chooseDirectory"

    def _fixresult(self, widget, result):
        if result:
            self.options["initialdir"] = result
        self.directory = result # compatibility
        return result


def askdirectory(**options):
    "Ask for a directory name"

    return apply(Chooser, (), options).show()

class Meter(Frame):
    '''A simple progress bar widget.'''
    def __init__(self, master, fillcolor='orchid1', text='',
            value=0.0, **kw):
        Frame.__init__(self, master, bg='white', width=350,
                height=20)
        self.configure(**kw)

        self._c = Canvas(self, bg=self['bg'],
                width=self['width'], height=self['height'],\
                        highlightthickness=0, relief='flat',
                        bd=0)
        self._c.pack(fill='x', expand=1)

        self._r = self._c.create_rectangle(0, 0, 0,
                int(self['height']), fill=fillcolor, width=0)
        self._t = self._c.create_text(int(self['width'])/2,
                int(self['height'])/2, text='')

        self.set(value, text)

    def set(self, value=0.0, text=None):
        if value < 0.0:
            value = 0.0
        elif value > 1.0:
            value = 1.0
        if text == None:
            text = str(int(round(100 * value))) + ' %'
            self._c.coords(self._r, 0, 0, int(self['width']) * value, int(self['height']))
            self._c.itemconfigure(self._t, text=text)

class App:
 
    def __init__(self, master):
        self.master = master
 
        #call start to initialize to create the UI elemets
        self.start()
 
    def start(self):
        self.master.title(u"Draugiem.LV vēstuļu lejupielādētājs'")
 
        self.now = datetime.datetime.now()
 
        #CREATE A TEXT/LABEL
        #create a variable with text
        #put "label01" in "self.master" which is the window/frame
        #then, put in the first row (row=0) and in the 2nd column (column=1), align it to "West"/"W"
        Label(self.master, text=u"e-pasts").grid(row=0, column=0, sticky=W)

        Label(self.master, text=u"parole").grid(row=1, column=0, sticky=W)
        #CREATE A TEXTBOX
        self.email = Entry(self.master)
        self.email["width"] = 20
        self.email.grid(row=0,column=1)
        self.password = Entry(self.master)
        self.password["width"] = 20
        self.password["show"] = "*"
        self.password.grid(row = 1, column = 1)
        #CREATE A BUTTON WITH "ASK TO OPEN A FILE"
        self.open_file = Button(self.master, text=u"Saglabāt...", command=self.browse_directory) #see: def browse_file(self)
        self.open_file.grid(row=2, column=1) #put it beside the filelocation textbox
        self.meter = Meter(self.master)
        self.meter.grid(row = 2, column = 1)
        #now for a button
        self.submit = Button(self.master, text="Lejupielādēt!", command=self.start_processing, fg="red")
        self.submit.grid(row=3, column=0)
        
    def start_processing(self):
        #more code here
        pass
    def browse_directory(self):
        self.directory = askdirectory(title=u"Izvēlies mapi...")
 
root = Tk()
app = App(root)
root.mainloop()
