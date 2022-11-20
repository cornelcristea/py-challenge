
# exercice 3
# please see the README.md file from main repository

from module import file_content
from sys import argv

if __name__ == '__main__':
    arguments = argv[1:]
    for arg in arguments:
        file_content(arg)
