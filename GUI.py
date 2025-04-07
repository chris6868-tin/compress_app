import FreeSimpleGUI as sg
import zip_creator as zc
import function
import os



label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="file")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key='folder')

label3 = sg.Text("Enter name of compressed file: ")
input3 = sg.Input(key="zipname")
compress_button = sg.Button("Compress")

label4 = sg.Text(key="output")

open_button = sg.Button("Open Folder", key="open_folder", visible=False)

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [label3, input3],
                           [compress_button, open_button],
                           [label4]])

last_folder_path = None
while True:
    event, value = window.read()
    print(value)

    if event == sg.WIN_CLOSED:
        break
    elif event == "Compress":
        filepaths_raw = value['file']
        filepaths = filepaths_raw.split(';') if filepaths_raw else []
        dest_dir = value['folder']
        compressed_file_name = value['zipname']

        if not filepaths_raw or not dest_dir or not compressed_file_name:
            window['output'].update(value='Please fill in all field!', text_color='red')
            continue

        if not function.is_valid_filename(compressed_file_name):
            window["output"].update(value="Invalid file name!", text_color="red")
            continue

        try:
            zc.make_archive(filepaths, dest_dir, compressed_file_name)
            window["output"].update(value="Compression succeeded!", text_color="green")
            window["open_folder"].update(visible=True)
            last_folder_path = os.path.join(dest_dir, compressed_file_name + ".zip")
        except Exception as e:
            window["output"].update(value=f"Eror: {e}", text_color='red')
    elif event == "open_folder" and last_folder_path:
        function.open_folder_in_explorer(last_folder_path)

window.close()

