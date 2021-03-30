#!/usr/bin/env python3

import shutil
import os

# set dir
os.chdir('/home/student/mycode/')

#move the file to the destination
shutil.move('raynor.obj', 'ceph_storage/')

# prompt the user for a new name
xname = input('What is the new name for kerrigan.obj ')

# rename the current kerrigan.obj file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
