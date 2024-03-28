import os
import shutil
from config import source_dir, destination_dir

def move_file(task, source_dir = source_dir, destination_dir = destination_dir):
    # Specify the destination directory where you want to move the .png files
    destination_dir = destination_dir + task.lower()
    # Make sure the destination directory exists, create it if not
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)    
    else:
        # Remove the directory and all its contents
        shutil.rmtree(destination_dir)
        os.makedirs(destination_dir)  

    # List all files in the source directory
    files = os.listdir(source_dir)

    # Loop through all files
    for file in files:
        # Check if the file is a .png file
        if file.endswith('.png'):
            # Construct full file path
            file_path = os.path.join(source_dir, file)
            
            # Move the .png file to the destination directory
            shutil.move(file_path, destination_dir)

    return destination_dir, os.listdir(destination_dir)
