#!/usr/bin/env python 
# encoding: utf-8
import sys
import pygtk
import gtk 

class Login(gtk.Window):
    def __init__(self):
        super(Login, self).__init__()
        self.set_title(u"ievadi lietotājvārdu un paroli")
        self.set_default_size(300, 170)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)
        username = gtk.Label(u"E-pasts")
        password = gtk.Label(u"Parole")
        directory = gtk.Label(u"mape")
        username_entry = gtk.Entry()
        password_entry = gtk.Entry()
        directory_entry = gtk.FileSelection()
        login_button = gtk.Button(u"pieteikties")
        login_button.connect("clicked", self.on_login)
        fixed = gtk.Fixed()
        fixed.put(username, 30, 20)
        fixed.put(password, 30, 50)
        fixed.put(username_entry, 100, 20)
        fixed.put(password_entry, 100, 50)
        fixed.put(directory, 30, 70)
        fixed.put(directory_entry, 100, 70)
        #fixed.put(login_button, 100, 100)
        password_entry.set_visibility(False)
        self.username=username_entry
        self.password=password_entry

        self.add(fixed)
        self.show_all()
    def on_login(self,login_button):
        if self.username.get_text()=="admin" and self.password.get_text()=="admin":
            window=gtk.Window(type=gtk.WINDOW_TOPLEVEL)
            window.set_title("successfully logged in")
            window.show()
        else:
            failed=gtk.Label("Invalid username/password")
            failed.show()

def main():
    gtk.main()
    return 0
if __name__=="__main__":
    Login()
    main()

