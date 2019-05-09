from setuptools import setup, find_packages
#import subprocess
import sys
import shutil
#import new_overlay
import glob
direc = "home/xilinx/"
files = glob.glob('*')
for i in range(len(files)): files[i] = direc+files[i] 

setup(
   name = "test",
   version = '1.0',
   url = 'https://github.com/adriankaisinclair/test',
   license = 'All right',
   author = "Adrian Sinclair",
   author_email = "aksincla@asu.edu",
   packages = find_packages(),
   package_data = {
   '' : files,
   },
   description = "test"
)
