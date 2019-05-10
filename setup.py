from setuptools import setup, find_packages
import sys
import shutil
import glob
direc = "home/xilinx/"
files = glob.glob('*')
#for i in range(len(files)): files[i] = direc+files[i] 

setup(
   name = "test",
   version = '1.0',
   url = 'https://github.com/adriankaisinclair/test',
   license = 'All right',
   author = "Adrian Sinclair",
   author_email = "aksincla@asu.edu",
   packages = [],
   package_data = {
   '' : ['*.txt','*.md'],
   },
   #data_files = [('../stuff',files)],
   description = "test"
)
