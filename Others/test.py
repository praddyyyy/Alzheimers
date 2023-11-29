import os
import random
import shutil

# Source directory containing the images
source_dir = r'D:\Alzheimers\Task1\Task1-Images\MRI\Images'

# Destination directory where you want to transfer the images
destination_dir = r'D:\Alzheimers\Voting2'

# Number of images to transfer
num_images_to_transfer = 10000

# Get a list of all image file names in the source directory
image_files = [file for file in os.listdir(source_dir) if file.endswith('.dcm')]

# Randomly select num_images_to_transfer files from the list
selected_files = random.sample(image_files, num_images_to_transfer)

# Transfer the selected files to the destination directory
for file in selected_files:
    source_path = os.path.join(source_dir, file)
    destination_path = os.path.join(destination_dir, file)
    shutil.copy(source_path, destination_path)

print(f"Transferred {num_images_to_transfer} random images from {source_dir} to {destination_dir}.")
