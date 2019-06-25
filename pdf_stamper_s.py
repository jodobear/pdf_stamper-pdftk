#!/usr/bin/python3

import subprocess
from os import listdir
from os.path import isdir, isfile, join

# print( \
# "This script batch stamps/watermarks pdf documents. \n \
# The script can do stamp and multistamp. Check documentation @ https://www.pdflabs.com/docs/pdftk-man-page/ \n\n \
# NOTE: Save this script in it's dedicated folder. The folder should only contain this script. \n \
# \n \
# Dependencies: \n \
# You need to install `pdftk` for this script to run. You can install it using \n \
# the following commands in the terminal: \n \
# \n \
#     $ sudo add-apt-repository ppa:malteworld/ppa \n \
#     $ sudo apt update \n \
#     $ sudo apt install pdftk \n \
# \n \
# You can find the repository for more information at: \n \
# https://gitlab.com/pdftk-java/pdftk \n \
# \n\n \
# Usage: \n \
#     $ python3 pdf_stamper.py \n\n \
# To make the script executable from terminal, enter in terminal: $ chmod u+x /path/to/file \n\n \
# Then use the following command to run the script from it's directory: $ ./pdf_stamper.py \n \
# \n \
# * Input the full path to relevant folders containing only relevant files. \n \
# * In case you want to do multistamp, enter the file name of the stamp, not the folder.\n \
# Filenames must start with 3 characters corresponding to the stamp filename you want to \n \
# stamp with. For multistamp, the filename need not follow the naming convention. \n \
# * The stamps have to be pdf documents containing the data you want to stamp. \n \
# \n \
# Example Filenames: \n \
#     To be stamped file: 001-abc.pdf \n \
#     Stamp file: 001.pdf \n")

# readme = open("./README.txt", 'r')
user_input = input()

# options[user_input]()

print("Enter full path to the folder containing files TO BE STAMPED:")
input_path = input()
print("\n Enter full path to the stamp file in case of multistamp or folder containing STAMP files:")
stamps_path = input()
print("\n Enter the full path to the OUTPUT folder:")
output_path = input()
print("\n Job to be done? Enter `stamp` or `multistamp`:")
# user_input = input()

print("To be stamped folder: ", input_path, '\n' \
        "Stamps file/folder: ", stamps_path, '\n' \
        "Output folder: ", output_path, '\n')

input_files = [f for f in listdir(input_path) if isfile(join(input_path, f))]

print("Input Files: ", input_files, '\n')

def help():
    '''Display help in terminal.'''
    # cmd = ["less", readme]
    # p = subprocess.run(cmd, stdout=subprocess.PIPE)
    user_input

def stamp(input_files):
    '''Stamp all pages of one pdf with corresponding stamp.pdf.'''

    stamp_files = [f for f in listdir(stamps_path) if isfile(join(stamps_path, f))]
    print("Stamp Files: ", stamp_files, '\n')
    for i in input_files:
        for j in stamp_files:
            if i[:3] == j[:3]:
                cmd = ["pdftk", f"{input_path}/{i}", "stamp", f"{stamps_path}/{j}", "output", f"{i}"]
                p = subprocess.run(cmd, stdout=subprocess.PIPE)
                if p.returncode != 0:
                    print("Plese check if you entered the correct path to directories and/or file.")

def multistamp(input_files):
    '''Stamp all pages of all files with one stamp.pdf.'''

    stamp_file = stamps_path
    print("Stamp File: ", stamp_file, '\n')
    for i in input_files:
        cmd = ["pdftk", f"{input_path}/{i}", "multistamp", f"{stamp_file}", "output", f"{i}"]
        p = subprocess.run(cmd, stdout=subprocess.PIPE)
        if p.returncode != 0:
            print("Plese check if you entered the correct path to directories and/or file.")

options = {"help" : help, "stamp" : stamp, "multistamp" : multistamp}  #, "background", "multibackground"]
options[user_input]()

def task(arg):
    '''Selector function for the task.'''
    if arg == "stamp":
        stamp(input_files)
    elif arg == "multistamp":
        multistamp(input_files)


output_files = [f for f in listdir(".") if isfile(join(".", f))]
print("Stamped files:")
for f in output_files:
    if f[-3:] == "pdf":
        print(f)

def move(output_path):
    for f in output_files:
        if f[-3:] == "pdf":
            cmd = ["mv", f, output_path]
            p = subprocess.run(cmd, stdout=subprocess.PIPE)

move(output_path)