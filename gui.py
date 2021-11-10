import PySimpleGUI as sg
import sys

folder_name = ""
image_number = 0
file_list_column = [
    [
        sg.Text("Save Images to (Choose a folder):"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Number of images: "),
        sg.In(size=(25, 1), enable_events=True, key="-NUMBER-")
    ],
    [
        sg.Button('start')
    ],
]

def start_gui():
    window = sg.Window("Image Generator", file_list_column)
    global folder_name
    global image_number
    # Run the Event Loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            sys.exit()
        if event == "start":
            break
        
        # Folder name was filled in, make a list of files in the folder
        if event == "-FOLDER-":
            folder_name = values["-FOLDER-"]
            
        if event == "-NUMBER-":
            image_number = values["-NUMBER-"]

    window.close()

    