import csv

# Path to the set.cfg file
cfg_file_path = r"C:\Users\rohht\Downloads\Трубы\Трубы\DATASET\metadata\test_set.cfg"

try:
    # Open the set.cfg file
    with open(cfg_file_path, 'r', encoding='cp1251') as file:
        lines = file.readlines()

    # Filter lines that contain ".frame"
    frame_lines = [line.strip() for line in lines if '.frame' in line]

    # Write these lines to testing_data.csv
    with open('testing_data2.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for line in frame_lines:
            writer.writerow([line])

except Exception as e:
    print(f"An error occurred: {e}")
