import os
import shutil
import csv

# Replace this with the actual path to your 'output.csv' file
csv_file_path = 'output.csv'

# Process each line in the CSV file
with open(csv_file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        original_file_path = row[0]
        second_value = row[1]
        third_value = row[2]
        folder_name = row[3]

        # change file_path's extension from .frame to .bmp
        original_file_path = original_file_path.replace('.frame', '.bmp') 

        # Add to original_file_path the base path
        original_file_path = os.path.join("C:\\rohhs\\lib\\tournament\\russian-rosatom-online-2023-12\\Technical\\DATASET\\FRAMES", original_file_path)

        # Extract the file name and create a new file name
        file_name = os.path.basename(original_file_path).split('.')[0]
        new_file_name = f"{file_name}{second_value}&{third_value}.bmp"

        # Create the directory if it does not exist
        new_folder_path = os.path.join("C:\\rohhs\\lib\\tournament\\russian-rosatom-online-2023-12\\Technical\\DATASET\\metadata\\content_bmp", folder_name)  # Adjust this path as needed
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        # Move the file
        new_file_path = os.path.join(new_folder_path, new_file_name)
        if os.path.exists(original_file_path):
            shutil.move(original_file_path, new_file_path)
        else:
            print(f"File not found: {original_file_path}")