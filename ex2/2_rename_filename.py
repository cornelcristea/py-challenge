
# exercice 2
# please see the README.md file from main repository

from datetime import datetime
from os import getcwd
from os.path import isfile
from os.path import isdir
from os.path import join
from os import listdir
from os import mkdir
from shutil import copyfile


current_year = datetime.now().year
current_dir = getcwd()

env_folder_name = 'env'
work_folder = join(current_dir, env_folder_name)

new_folder_name = 'renamed_files'
new_folder = join(work_folder, new_folder_name)

if not isdir(new_folder):
    mkdir(new_folder)
    print(new_folder_name, 'folder has been created in', env_folder_name)
else:
    print(new_folder_name, 'folder already exist in', env_folder_name, '. No creation needed')

all_files = listdir(work_folder)
for file in all_files:
    if not file == new_folder_name: # ignore renamed_files folder if it's already present
        sf = file.split('.')
        file_ext = sf[1]
        idx_file = all_files.index(file)
        new_name = 'file_' + str(current_year) + '_' + str(idx_file) + '.' + file_ext
        src_path = work_folder + '/' + file
        dst_path = new_folder + '/' + new_name
        if isfile(dst_path):
            print('File', new_name, 'already exist in', new_folder, 'folder')
        else:
            try:
                copyfile(src_path, dst_path)
                print('File', file, 'has been renamed with the new name', new_name)
                print('File', new_name, 'has been copied in', new_folder_name, 'folder')
            except ValueError:
                print(ValueError)
        