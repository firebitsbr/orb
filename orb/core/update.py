#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
This file is part of the orb project, http://orb.03c8.net

Orb - 2016/2017/2018 - by psy (epsylon@riseup.net)

You should have received a copy of the GNU General Public License along
with RedSquat; if not, write to the Free Software Foundation, Inc., 51
Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
import os
from subprocess import PIPE
from subprocess import Popen as execute
        
class Updater(object):
    """     
    Update Orb automatically from a .git repository
    """     
    def __init__(self):
        GIT_REPOSITORY = "https://github.com/epsylon/orb"
        rootDir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', ''))
        if not os.path.exists(os.path.join(rootDir, ".git")):
            print "Not any .git repository found!\n"
            print "="*30
            print "\nTo have working this feature, you should clone Orb with:\n"
            print "$ git clone %s" % GIT_REPOSITORY
        else:
            checkout = execute("git checkout . && git pull", shell=True, stdout=PIPE, stderr=PIPE).communicate()[0]
            print checkout
            if not "Already up-to-date" in checkout:
                print "Congratulations!! Orb has been updated... ;-)\n"
            else:
                print "Your Orb doesn't need to be updated... ;-)\n"
