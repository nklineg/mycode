#!/usr/bin/env python3

import shutil
import os

# move into the working dir
os.chdir("/home/student/mycode/")

# copy file
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#copy dir
shutil.copytree("5g_research/", "5g_research_backup/")
