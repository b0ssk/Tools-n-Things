# Create Project Tree for assets based on DCC
# Jon Parkins April 22, 2024.
# Python 3.12
# Version 1.0

import os

# Globals for use in functions
DIRECTORIES = []
FULL_DIRECTORY = []
DIR_COUNT = 0


def find_dirs():
    # creates list of all files and directories in current location

    global DIR_COUNT
    global DIRECTORIES
    global FULL_DIRECTORY

    dir_list = os.listdir('.')

    # lists full path to current directory
    root_dir = os.path.abspath(os.curdir)

    # separate out directories from files and print list
    DIRECTORIES = [dirs for dirs in dir_list if os.path.isdir(dirs)]
    FULL_DIRECTORY = []
    # separate out from files
    for directory in DIRECTORIES:
        FULL_DIRECTORY.append(root_dir + '/' + directory)

    # Add Create, Back and Exit options
    FULL_DIRECTORY.append('CREATE PROJECT')
    FULL_DIRECTORY.append('BACK')
    FULL_DIRECTORY.append('EXIT')

    # print list of directories
    dir_list = [0]
    for element in FULL_DIRECTORY:
        print(f"{DIR_COUNT}. {element}")
        DIR_COUNT += 1
        dir_list.append(DIR_COUNT)


def change_dirs():
    # Change directories function, calls the find directories function, both need to use the same vars for names so set
    # as globals, and resets on each directory scan.

    global DIRECTORIES
    global DIR_COUNT
    global FULL_DIRECTORY

    while True:
        find_dirs()
        dir_num = input("\nWhat directory would you like to change to? Select a #: ")

        if dir_num.isdigit():
            # convert to int
            dir_num = int(dir_num)
            if dir_num >= 0 and dir_num in range(DIR_COUNT + 1):
                if dir_num == len(FULL_DIRECTORY) - 1:
                    return False
                elif dir_num == len(FULL_DIRECTORY) - 2:
                    os.chdir('..')
                    DIRECTORIES = []
                    DIR_COUNT = 0
                    FULL_DIRECTORY = []
                elif dir_num == len(FULL_DIRECTORY) - 3:
                    make_dirs()
                else:
                    os.chdir(DIRECTORIES[dir_num])
                    print(f"\nCurrent directory: {os.getcwd()}\n")
                    DIRECTORIES = []
                    DIR_COUNT = 0
                    FULL_DIRECTORY = []
            else:
                print("\nEnter a numerical selection from the list.\n")
                DIRECTORIES = []
                DIR_COUNT = 0
                FULL_DIRECTORY = []
        else:
            print("\nEnter a numerical selection from the list.\n")
            DIRECTORIES = []
            DIR_COUNT = 0
            FULL_DIRECTORY = []


def make_dirs():
    # populate list with directory names to check if project already exists
    global DIRECTORIES
    global DIR_COUNT
    global FULL_DIRECTORY

    while True:
        dir_check = []

        for dir_name in os.listdir('.'):
            dir_check.append(dir_name)

        proj = input("Enter project name: ")

        if proj in dir_check:
            print("\nThis name already exists, please enter a different one\n")
        else:
            # Reference
            reference = proj + "/" + "Reference"
            os.makedirs(reference)

            # ZBrush Directories
            zbrush_sub01 = "ZBrush/WIP"
            zbrush_sub02 = "ZBrush/Export"
            proj_path01 = proj + "/" + zbrush_sub01
            proj_path02 = proj + "/" + zbrush_sub02
            os.makedirs(proj_path01)
            os.makedirs(proj_path02)

            # Texture Directories
            text_sub01 = "Texture/WIP"
            text_sub02 = "Texture/Export"
            proj_path01 = proj + "/" + text_sub01
            proj_path02 = proj + "/" + text_sub02
            os.makedirs(proj_path01)
            os.makedirs(proj_path02)

            # Maya Directories
            print("Use Maya Set Project to create Maya directory structure")
            DIRECTORIES = []
            DIR_COUNT = 0
            FULL_DIRECTORY = []
            return False


change_dirs()
