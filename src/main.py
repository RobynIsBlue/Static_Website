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

    # split_from = from_path.split("/")
    # split_dest = dest_path.split("/")
    # if len(split_dest) > 1:
    #     new_path = "/".join(split_dest)
    # else:
    #     new_path = "/" + split_dest[0]
    with open(dest_path, "w") as f:
        f.write(replace_2)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    split_dir_path_content = dir_path_content.split("/")
    add_to_new_dir = dir_path_content
    if os.path.isfile(dir_path_content):
        split_file = split_dir_path_content[-1]
        file = split_file.split(".")[0]
        extension = split_file.split(".")[-1]
        if extension == "md":
            generate_page(dir_path_content, template_path, dest_dir_path + "/" + file + ".html")
    else:
        for file_or_dir in os.listdir(dir_path_content):
            if len(split_dir_path_content) > 1:
                os.mkdir(dest_dir_path + "/" + dir_path_content.split("/")[-1])
                add_to_new_dir = "/".join(dir_path_content.split("/")[1:])    
                generate_pages_recursive(dir_path_content + "/" + file_or_dir, template_path, dest_dir_path + "/" + add_to_new_dir)
            else:
                generate_pages_recursive(dir_path_content + "/" + file_or_dir, template_path, dest_dir_path)

    

def main():
    shutil.rmtree("public")
    os.mkdir("public")
    recurring_files_to_dest("static", "public")
    generate_pages_recursive("content", "template.html", "public")

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
