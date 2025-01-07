from textnode import *
from markdowns import *

import os
import shutil

def recurring_files_to_dest(from_x, to_dir):
    if os.path.isfile(from_x):
        print("from: " + str(from_x))
        shutil.copy(from_x, to_dir)
        return
    dir_name = from_x.split("/")[-1]
    joined_paths = to_dir
    if len(from_x.split("/")) != 1:
        joined_paths = os.path.join(to_dir, dir_name)
        os.mkdir(joined_paths)
    for file_or_dir in os.listdir(from_x):
        new_file_or_dir = os.path.join(from_x, file_or_dir)
        recurring_files_to_dest(new_file_or_dir, joined_paths)

def plus_delete(from_dir, to_dir):
    shutil.rmtree(to_dir)
    os.mkdir(to_dir)
    recurring_files_to_dest(from_dir, to_dir)

def extract_title(markdown):
    read_file = open(markdown).read()
    for line in read_file.split("\n"):
        if line.startswith("# "):
            return line[2:]
        

# Having issues writing a new HTML file and possibly creating new directories.
# From_path plugged into template path, then located to dest_path.
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    read_from_path = open(from_path).read()
    read_template_path = open(template_path).read()

    new_first = markdown_to_html_node(read_from_path)
    string_new_first = new_first.to_html()
    title = extract_title(from_path)
    replace_1 = read_template_path.replace("{{ Title }}", title)
    replace_2 = replace_1.replace("{{ Content }}", string_new_first)
    split_from = from_path.split("/")
    split_dest = dest_path.split("/")

    # for x in range(len(split_dest)):
    #     if split_dest[0] != split_from[:-1]:
    #         break
    #     split_from.pop()
    #     split_dest(0)
    # new_list = split_dest[:-1] + split_from[:-1] + split_dest[-1:]
    # newer_list = "/".join(new_list[:-1])
    # os.makedirs(newer_list)
    # newerer_list = "/".join(new_list)

    with open(dest_path, "w") as f:
        f.write(replace_2)

def main():
    shutil.rmtree("public")
    os.mkdir("public")
    recurring_files_to_dest("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
