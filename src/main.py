from textnode import *

import os
import shutil

def recurring_files_to_dest(from_x, to_dir):
    if os.path.isfile(from_x):
        print("from: " + str(from_x))
        shutil.copy(from_x, to_dir)
        return
    dir_name = from_x.split("/")[-1]
    joined_paths = os.path.join(to_dir, dir_name)
    os.mkdir(joined_paths)
    for file_or_dir in os.listdir(from_x):
        new_file_or_dir = os.path.join(from_x, file_or_dir)
        recurring_files_to_dest(new_file_or_dir, joined_paths)

def plus_delete(from_dir, to_dir):
    shutil.rmtree(to_dir)
    os.mkdir(to_dir)
    recurring_files_to_dest(from_dir, to_dir)


def main():
    plus_delete("static", "public")

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
