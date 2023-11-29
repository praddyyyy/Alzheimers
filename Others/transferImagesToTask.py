import os
import shutil

source_folder = r"D:\Research\Neurodegenerative Diseases\Images\fMRI-Images\MCI\ADNI"  # Replace with the actual path to the source folder
destination_folder = r"D:\Research\Neurodegenerative Diseases\Images\Task1\Task1-Images\fMRI"  # Replace with the actual path to the destination folder

# Iterate over the patient folders
for patient_folder in os.listdir(source_folder):
    patient_folder_path = os.path.join(source_folder, patient_folder)
    if os.path.isdir(patient_folder_path):
        # Iterate over the MRI image files within the patient folder
        for image_file in os.listdir(patient_folder_path):
            if image_file.endswith(".dcm"):  # Assuming the MRI image files have the ".dcm" extension
                image_number = image_file.split("_")[-3].split(".")[0] 
                #ADNI_002_S_5018_PT_ADNI_Brain_PET__Raw_FDG_br_raw_20121114100924090_224_S174525_I346569
                print(image_number)
                disease = "MCI"  # Replace with the actual disease name
                
                # Generate the destination filename using the desired naming convention
                destination_filename = f"{patient_folder}_fMRI_{image_number}_{disease}.dcm"
                
                # Copy the image file to the destination folder with the new filename
                source_path = os.path.join(patient_folder_path, image_file)
                destination_path = os.path.join(destination_folder, destination_filename)
                shutil.copyfile(source_path, destination_path)