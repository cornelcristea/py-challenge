
# Write a module wich contains a function with a variable number of files as argument
# Execute this script from terminal and set the name of text files as arguments for this
# The content of files should be show in terminal

# Terminal command: python 3_file_content.py file_1 file_2 file_3 file_4 file_5

# Remark: I did not knew how to implement this but I created a module which 
# will display the content of a file and in the main file I called this module in a FOR loop 
# to be able to read all file which are defined as arguments

from module import file_content
from sys import argv

if __name__ == '__main__':
    arguments = argv[1:]
    for arg in arguments:
        file_content(arg)
