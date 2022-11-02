
from os import getcwd
from os.path import join

def file_content(file):
    work_folder = join(getcwd() + '\env')
    if '.txt' in file:
        file_path = join(work_folder, file)
    else:
        file_path = join(work_folder, (file + '.txt'))

    f = open(file_path, "r")
    print()
    print('=======================================')
    print(file_path)
    print('=======================================')
    print(f.read())
    print()
