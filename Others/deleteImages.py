import os
import shutil

root_directory = r'D:\Research\Neurodegenerative Diseases\Images\fMRI-Images\AD\ADNI'

def delete_images_except_range(patient_folder):
    if os.path.isdir(patient_folder):
        for file_name in os.listdir(patient_folder):
            if file_name.endswith('.dcm'):
                frame_number = int(file_name.split('_')[-3])
                if not (2500 <= frame_number <= 3500):
                    file_path = os.path.join(patient_folder, file_name)
                    os.remove(file_path)  # Delete the file

def filter_and_copy_images(source_dir, destination_dir):
    for patient_id in os.listdir(source_dir):
        patient_folder = os.path.join(source_dir, patient_id)
        delete_images_except_range(patient_folder)

filter_and_copy_images(root_directory, root_directory)
