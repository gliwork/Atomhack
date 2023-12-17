import os

# Define the folder path
folder_path = r"C:\rohhs\lib\tournament\russian-rosatom-online-2023-12\Technical\DATASET\metadata\content"

# Walk through the folder
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # Check if the file extension is '.frame'
        if file.endswith('.frame'):
            # Construct the old file path
            old_file = os.path.join(root, file)
            # Change the extension to '.bmp'
            new_file = os.path.join(root, file[:-6] + '.bmp')
            # Rename the file
            os.rename(old_file, new_file)

# The script will rename all files with the .frame extension to .bmp in the specified folder and its subfolders.
