from textnode import *

import os
import shutil

def recurring_files_to_dest(from_dir, to_dir):
    if os.path.isfile(from_dir):
        print("from: " + str(from_dir))
        return shutil.copy(from_dir)
    new_path = os.mkdir(shutil.copy(from_dir))
    new_path = os.path.join(new_path, from_dir)
    for file_or_dir in os.listdir(from_dir):
        recurring_files_to_dest(file_or_dir, to_dir)

def plus_delete(from_dir, to_dir):
    shutil.rmtree(to_dir)
    recurring_files_to_dest(from_dir, to_dir)


def main():
    plus_delete("../static", "../public")

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
