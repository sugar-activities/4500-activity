#!/usr/bin/env python
# PiTiVi , Non-linear video editor
#
#       pitivi
#
# Copyright (c) 2005, Edward Hervey <bilboed@bilboed.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import os, sys, string, locale, gettext, gobject, gst, pygst, gtk, pygtk, threading
#pygst.require('0.10')
from gtk import glade

from sugar.activity import activity

# variables
CONFIGURED_PYTHONPATH = ''
LIBDIR = '/home/olpc/Activity/Pitivy.activity/'

localedir = ""

def _add_pitivi_path():
	global localedir
	directorio = os.path.dirname(os.path.abspath(__file__))

	root = os.path.join(LIBDIR, 'pitivi')
	localedir = "/home/olpc/Activity/Pitivy.activity/"

	if not root in sys.path:
		sys.path.insert(0, root)

	for path in string.split(CONFIGURED_PYTHONPATH, ':'):
		if path not in sys.path:
		    sys.path.insert(0, path)
	
	#print "Directorios:", root, localedir
	
def _init_gobject_gtk_gst():
	global localedir
	gobject.threads_init()
	glade.bindtextdomain('pitivi', localedir)

def _run_pitivi():
	import pitivi.application as ptv
	#sys.exit(ptv.main(sys.argv))
	ptv.main(sys.argv)

def RunPitivy():
	try:
	    _add_pitivi_path()
	    _init_gobject_gtk_gst()
	    _run_pitivi()
	except KeyboardInterrupt:
	    print "Interrupted by user!"

class PitiviActivity(activity.Activity):
	def __init__(self, handle):
		activity.Activity.__init__(self, handle, False)
		# PitiviJAM
		self.set_canvas(gtk.VBox())
		self.show_all()

		_add_pitivi_path()
	    	_init_gobject_gtk_gst()
		#_run_pitivi()
		thread = threading.Thread( target=_run_pitivi )
		thread.start()

if __name__=="__main__":
	RunPitivy()

