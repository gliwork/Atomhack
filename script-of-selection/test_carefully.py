import csv

# File paths
set_cfg_path = 'set.cfg'
found_path = 'found.csv'
output_path = 'output.csv'

try:
    # Read filenames from found.csv
    with open(found_path, 'r', encoding='utf-8') as file:
        found_filenames = [line.strip() for line in file]

    # Process set.cfg
    with open(set_cfg_path, 'r', encoding='cp1251') as file:
        lines = file.readlines()

    # Prepare to write to the output CSV
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Variable to track if the current line is a filename we're interested in
        current_filename = None

        for line in lines:
            line = line.strip()
            if line in found_filenames:
                current_filename = line  # Update the current filename
            elif current_filename:
                # Check if the line is not another filename
                if not line.endswith('.frame'):
                    # This is a value line associated with the current filename
                    values = line.split(', ')
                    writer.writerow([current_filename, *values])
                else:
                    # Reset current_filename if it's another filename
                    current_filename = None

except Exception as e:
    print(f"An error occurred: {e}")
