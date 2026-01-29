#Program for Creating a folder
#OSFolderCreateEx.py
import os
try:
    #os.mkdir("PYTHON")
    os.rmdir("PYTHON")
    print("Folder Created--verify")
except FileExistsError:
    print("Folder already Exists")
except FileNotFoundError:
    print("Root Folder Does Not Exist")