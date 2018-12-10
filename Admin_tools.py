import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess
class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Admin Tools")
        self.set_border_width(3)
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
        #Settings buttons
        settings_button1 = Gtk.Button(label='Bash')
        settings_button2 = Gtk.Button(label='Grub')
        settings_button3 = Gtk.Button(label='Sudoers')
        settings_button4 = Gtk.Button(label='Fstab')
        settings_button5 = Gtk.Button(label='TLP')
        settings_button6 = Gtk.Button(label='Ansible')
        settings_button7 = Gtk.Button(label='UDEV')
        #tools buttons
        tools_button1 = Gtk.Button(label='Bash')


        #settings_button1.connect("clicked",self.bash_clicked())

        tools_button2 = Gtk.Button(label='ssh')
        tools_button3 = Gtk.Button(label='htop')
        tools_button4 = Gtk.Button(label='Vim')
        tools_button5 = Gtk.Button(label='tmux')
        tools_button6 = Gtk.Button(label='list')
        #about buttons
        about_button1 = Gtk.Button(label='About')
    
        tools_button1.connect("clicked",self.open_clicked)
        tools_button2.connect("clicked",self.open_clicked)
        tools_button3.connect("clicked",self.open_clicked)
        tools_button4.connect("clicked",self.open_clicked)
        tools_button5.connect("clicked",self.open_clicked)
        tools_button6.connect("clicked",self.open_clicked)
        settings_button1.connect("clicked",self.open_clicked)
        settings_button2.connect("clicked",self.open_clicked)
        settings_button3.connect("clicked",self.open_clicked)
        settings_button4.connect("clicked",self.open_clicked)
        settings_button5.connect("clicked",self.open_clicked)
        settings_button6.connect("clicked",self.open_clicked)
        settings_button7.connect("clicked",self.open_clicked)
#Page 1
        self.page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label('Tools'))
        self.notebook.append_page(self.page1, Gtk.Label(label='Tools'))
        self.page1.pack_start(tools_button1, True, True, 0)
        self.page1.pack_start(tools_button2, True, True, 0)
        self.page1.pack_start(tools_button3, True, True, 0)
        self.page1.pack_start(tools_button4, True, True, 0)
        self.page1.pack_start(tools_button5, True, True, 0)
        self.page1.pack_start(tools_button6, True, True, 1)
#grid in page 1

#page 3

        self.page3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.page3.set_border_width(10)
        self.page3.add(Gtk.Label('Settings'))
        self.notebook.append_page(self.page3, Gtk.Label('Settings'))
#Buttons page 3


        self.page3.pack_start(settings_button1, True, True, 0)
        self.page3.pack_start(settings_button2, True, True, 0)
        self.page3.pack_start(settings_button3, True, True, 0)
        self.page3.pack_start(settings_button4, True, True, 0)
        self.page3.pack_start(settings_button5, True, True, 0)
        self.page3.pack_start(settings_button6, True, True, 1)
        self.page3.pack_start(settings_button7, True, True, 1)


        self.help_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.help_page.set_border_width(10)
        self.notebook.append_page(
            self.help_page,
            Gtk.Image.new_from_icon_name(
                "help-about",
                Gtk.IconSize.MENU
            )
        )
        self.help_page.pack_start(about_button1, True, True, 0)
        about_button1.connect("clicked",self.about_clicked)
    def about_clicked(self, widget):
        diaglog = PopUp(self)
        response = dialog.run()
        dialog.destroy()
    def open_clicked(self, widget):
        diaglog = Openning_programs(self)
        response = dialog.run()
        dialog.destroy()

class PopUp(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "About", parent)
        self.set_border_width(10)
        self.set_default_size(200,120)
        area = self.get_content_area()
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "HeaderBar example"
        self.set_titlebar(hb)
        self.notebook = Gtk.Notebook()
        area.add(self.notebook)

        self.aboutpage = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.aboutpage.set_border_width(10)
        self.aboutpage.add(Gtk.Label('About'))
        self.notebook.append_page(self.aboutpage, Gtk.Label('About'))
        self.aboutpage.add(Gtk.Label('This is Admin Tools.\nIt is designed to help people find and change settings of common files\n Most settings do not have a GUI. Thus I created this program to help find them.\n'))


        self.lisencepage = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.lisencepage.set_border_width(10)
        self.notebook.append_page(self.lisencepage, Gtk.Label('License'))
        self.lisencepage.add(Gtk.Label('License\nAdmin Tools is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by\nthe Free Software Foundation; either version 2 of the License, or\n(at your option) any later version.\nAdmin Tools is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the\nGNU General Public License formore details.\nYou should have received a copy of the GNU General Public License\nalong with Admin Tool; if not, write to the Free Software Foundation, Inc.,\n51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA'))
        self.show_all()


class Openning_programs(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Program", parent)
        self.set_border_width(10)
        self.set_default_size(200,120)
        area = self.get_content_area()
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Open Program"
        self.set_titlebar(hb)
        self.notebook = Gtk.Notebook()
        area.add(self.notebook)

        self.Open_Program = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.Open_Program.set_border_width(10)
        self.Open_Program.add(Gtk.Label('Open Program'))
        self.notebook.append_page(self.Open_Program, Gtk.Label('Open program'))
        self.show_all()

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

