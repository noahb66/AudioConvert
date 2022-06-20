import PySimpleGUI as sg
from audioConvert3 import audio_convert

layout = [[sg.Text('Folder', size=(15, 1), auto_size_text=False, justification='right'),
           sg.InputText('Default Folder'), sg.FolderBrowse(key='-FOLDER-')],
          [sg.Text('Output Folder', size=(15, 1), auto_size_text=False, justification='right'),
           sg.InputText('Output Folder'), sg.FolderBrowse(key='-OUTPUT-')],
          [sg.Text('Choose original file type', size=(15, 1)),
           sg.InputCombo(('wav', 'mp3', 'aif', 'aiff', 'flac', 'RAW'), size=(20, 3), key=('-ORIGINAL-'))],
          [sg.Text('Choose new file type', size=(15, 1)),
           sg.InputCombo(('wav', 'mp3', 'aiff', 'flac', 'RAW'), size=(20, 3), key=('-NEW FILE TYPE-'))],
          [sg.Submit('Convert'), sg.Cancel()]
          ]

window = sg.Window('Audio Converter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Convert':
        folder = values['-FOLDER-']
        original = values['-ORIGINAL-']
        new_file_type = values['-NEW FILE TYPE-']
        output = values['-OUTPUT-']
        audio_convert(folder, original, new_file_type, output)
window.close()

