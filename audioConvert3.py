# This program will convert selected directory into a specific audio file type 
from pydub import AudioSegment
import glob
from pathlib import Path


def audio_convert(folder, original, new_file_type, output):
    number = 0
    directory = folder
    og_file = original
    file_type = new_file_type
    directory = directory + '/*' + '.' + og_file
    output_dir = output
    print(directory)
    for file in glob.iglob(directory):  # iterates through the directory
        path = Path(file)  # Gets file name
        print(path)
        name = '{}.{}'.format(path.stem, file_type)
        print(name)
        if og_file == 'aif':
            og_file = 'aiff'
        sound = AudioSegment.from_file(path, format=og_file)
        export = sound.export(output_dir + '/' + name, format=file_type) 
        print('Writing file number....', number)
        number += 1 

