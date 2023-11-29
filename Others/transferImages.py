import os
import shutil

root_directory = r'D:\Research\Neurodegenerative Diseases\Images\fMRI-Images\LMCI\ADNI'

def filter_and_copy_images(source_dir, destination_dir):
    for patient_id in os.listdir(source_dir):
        patient_folder = os.path.join(source_dir, patient_id)
        if os.path.isdir(patient_folder):
            axial_t2_flair_folders = os.listdir(os.path.join(patient_folder, 'Resting_State_fMRI'))
            if axial_t2_flair_folders:
                last_folder = os.path.join(patient_folder, 'Resting_State_fMRI', axial_t2_flair_folders[-1])
                sub_folders = os.listdir(last_folder)
                if sub_folders:
                    last_sub_folder = os.path.join(last_folder, sub_folders[-1])
                    for file_name in os.listdir(last_sub_folder):
                        if file_name.endswith('.dcm'):
                            frame_number = int(file_name.split('_')[-3])
                            if 2000 <= frame_number <= 4500:
                            # if 100 <= frame_number <= 350:
                            # if 5 <= frame_number <= 30: MRI
                                source_path = os.path.join(last_sub_folder, file_name)
                                destination_path = os.path.join(patient_folder, file_name)
                                shutil.copy(source_path, destination_path)

filter_and_copy_images(root_directory, root_directory)

