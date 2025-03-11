import os
import glob
import tkinter as tk
from tkinter import filedialog
import argparse


def close_if_open(file_path):
    """Closes the file if it's open."""
    try:
        with open(file_path, 'r') as f:
            # File is open, so close it
            f.close()
            print(f"{file_path} was open and has been closed.")
    except FileNotFoundError:
        print(f"{file_path} is not open.")

# Example usage:
parser = argparse.ArgumentParser(description='aggregates transcription for srts in specified modules folder')
parser.add_argument('modulenum', metavar = 'modulenum', type = int, help = 'enter the module number')
args = parser.parse_args()
folder = "Module "+ str(args.modulenum)
current_directory = os.getcwd() 
# os.path.dirname(os.path.abspath(__file__))

# root = tk.Tk()
# root.withdraw()
# directory = filedialog.askdirectory()
extension = ".srt"
# print(folder_path)

# file_path = filedialog.askopenfilename()

# data_list = []
# with open(file_path, 'r') as file:
#     for line in file:
#         line = line.replace('\n','').strip()
#         if line and not line[0].isdigit():
#             data_list.append(line)

# text = " ".join(data_list)
# print(text)
destination_directory = current_directory+"\\"+folder
output_path = destination_directory+"\\output.txt"
close_if_open(output_path)
if os.path.exists(output_path):
    os.remove(output_path)
for file_path in glob.glob(f'{destination_directory}/**/*{extension}', recursive=True):
    data_list = [file_path,"\n"]
    with open(file_path,'r') as file:
        for line in file:
            line = line.replace('\n',"").strip()
            if line and not line[0].isdigit():
                data_list.append(line)

    data_list.append("\n\n")
    text = " ".join(data_list)
    with open(output_path, 'a') as outputfile:
        outputfile.write(text)
    
os.system("notepad.exe "+output_path)
            
        # # text = file.read() # text is a string data type
        # text_list = file.read().split('\n') # text is an array
        # print("before:\n", text_list)
        # print(file_path,"\n")
        # for index, line in enumerate(text_list):
        #     if line: print(index, line)
        #     # if line and line[0].isdigit():
        #     #     print("removed", line)
        #     #     text_list.remove(line)
        # print("after:\n",text_list)
        #     # line = line.strip()
        #     # if not line:
        #     #     text_list.remove(line)
        #     # if line and line[0].isdigit():
        #     #     # print(line)
        #     #     text_list.remove(line)
        # # text = " ".join(text_list)
        # # print(file_path,'\n',text_list,'\n')
    