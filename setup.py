from setuptools import setup, find_packages
import sys
import os
import shutil

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
os.rename('test','/home/xilinx/test')
print("Done downloading test from git!")
