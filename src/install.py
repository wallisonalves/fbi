#!/usr/bin/env python
#
# Copyright (c) 2013 Eric Turgeon
#
# See COPYING for licence terms.
#
# install.py v 0.4 Sunday, February 08 2015 Eric Turgeon
#
# install.py give the job to pc-sysinstall to install FreeBSD.
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import threading
import os
from subprocess import Popen, PIPE, STDOUT, call
from time import sleep
from partition_handler import rDeleteParttion, destroyParttion, makingParttion
from create_cfg import fbsd_cfg
from slides import fbsdSlides
import sys
installer = "/usr/local/lib/fbi/"
sys.path.append(installer)
tmp = "/tmp/.fbi/"
fbi_path = "/usr/local/lib/fbi/"
sysinstall = "/usr/local/sbin/pc-sysinstall"
rcconffbsd = "/etc/rc.conf.freebsd"
default_site = "/usr/local/lib/fbi/slides/welcome.html"
logo = "/usr/local/lib/fbi/logo.png"


def update_progess(probar, bartext):
    new_val = probar.get_fraction() + 0.000003
    probar.set_fraction(new_val)
    probar.set_text(bartext[0:80])


def read_output(command, probar):
    call('service hald stop', shell=True)
    call('umount /media/FreeBSD', shell=True)
    GLib.idle_add(update_progess, probar, "Creating pcinstall.cfg")

    # If rc.conf.freebsd run fbsd_cfg
    if os.path.exists(rcconffbsd):
        fbsd_cfg()
        sleep(1)
    if os.path.exists(tmp + 'delete'):
        GLib.idle_add(update_progess, probar, "Deleting partition")
        rDeleteParttion()
        sleep(1)
    # destroy disk partition and create scheme
    if os.path.exists(tmp + 'destroy'):
        GLib.idle_add(update_progess, probar, "Creating disk partition")
        destroyParttion()
        sleep(1)
    # create partition
    if os.path.exists(tmp + 'create'):
        GLib.idle_add(update_progess, probar, "Creating new partitions")
        makingParttion()
        sleep(1)
    p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE,
              stderr=STDOUT, close_fds=True)
    while True:
        line = p.stdout.readline()
        if not line:
            break
        bartext = line.rstrip()
        GLib.idle_add(update_progess, probar, bartext)
        # Those for next 4 line is for debugin only.
        # filer = open("/tmp/.fbi/tmp", "a")
        # filer.writelines(bartext)
        # filer.close
        print(bartext)
    call('service hald start', shell=True)
    if bartext.rstrip() == "Installation finished!":
        Popen('python2 %send.py' % fbi_path, shell=True, close_fds=True)
        call("rm -rf /tmp/.fbi/", shell=True, close_fds=True)
        Gtk.main_quit()
    else:
        Popen('python2 %serror.py' % fbi_path, shell=True, close_fds=True)
        Gtk.main_quit()


class installSlide():

    def close_application(self, widget, event=None):
        Gtk.main_quit()

    def __init__(self):
        self.mainHbox = Gtk.HBox(False, 0)
        self.mainHbox.show()

        self.mainVbox = Gtk.VBox(False, 0)
        self.mainVbox.show()
        self.mainHbox.pack_start(self.mainVbox, True, True, 0)
        slide = fbsdSlides()
        getSlides = slide.get_slide()
        self.mainVbox.pack_start(getSlides, True, True, 0)

    def get_model(self):
        return self.mainHbox


class installProgress():

    def __init__(self):
        self.pbar = Gtk.ProgressBar()
        self.pbar.set_show_text(True)
        command = '%s -c %spcinstall.cfg' % (sysinstall, tmp)
        thr = threading.Thread(target=read_output,
                               args=(command, self.pbar))
        thr.setDaemon(True)
        thr.start()
        self.pbar.show()

    def getProgressBar(self):
        return self.pbar
