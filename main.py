import os
import shutil

common_img = ['.apng', '.avif', '.gif', '.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.png', '.svg', '.webp', '.bmp' +
              '.ico', '.cur', '.tif', '.tiff']
common_doc = ['.doc', '.docx', '.html', '.htm', '.odt', '.pdf', '.xls', '.xlsx', '.csv', '.ods', '.txt']

files = []


# Input example: C:\Users\Lucas\Downloads
# Expected output: C:\\Users\\Lucas\\Downloads
def edit_path(local_path):
    on_edit = ''
    for char in local_path:
        if char == '\\':
            on_edit += '\\\\'
        else:
            on_edit += char
    local_path = on_edit
    return local_path


def listdir(local_path):
    for file in os.listdir(local_path):
        print(file)


def add_to_files(extensions):
    global edited_path
    global files
    files = []
    for file in os.listdir(edited_path):
        for extension in extensions:
            if extension in file:
                files.append(file)


def move_files(this_files):
    global edited_path
    for file in this_files:
        shutil.move(edited_path + '\\\\' + file, 'C:\\Users\\Lucas\\Desktop\\Images')


# Input example: C:\Users\Lucas\Downloads
path = input("Insert the full path of the directory you want to check: ")
edited_path = edit_path(path)
add_to_files(common_img)
move_files(files)