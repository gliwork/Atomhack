import os
import csv

try:
    # Define the directory path
    directory_path = r"C:\Users\rohht\Downloads\Трубы\Трубы\DATASET\FRAMES\/"

    # Walk through the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Construct full file path
            file_path = os.path.join(root, file)
            # Append file paths to test_files.csv file in the current directory with windows1251 encoding
            with open('test_files.csv', 'a', encoding='utf-8', newline='') as f:
                # write only files with .frame extension
                if file_path.endswith(".frame"):
                    # remove "C:\Users\rohht\Downloads\Трубы\Трубы\DATASET\FRAMES\" from the file path
                    file_path = file_path.replace(directory_path , '')
                    # write file path to csv file
                    writer = csv.writer(f)
                    writer.writerow([file_path])

except Exception as e:
    print(f"An error occurred: {e}")
