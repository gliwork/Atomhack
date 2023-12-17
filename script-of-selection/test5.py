import csv

# File paths
testing_data2_path = 'testing_data2.csv'
testing_data_path = 'testing_data.csv'
difference_from_path = 'difference_from.csv'
difference_to_path = 'difference_to.csv'

try:
    # Read contents of testing_data.csv
    with open(testing_data_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        testing_data = set(tuple(row) for row in reader)

    # Read contents of testing_data2.csv
    with open(testing_data2_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        testing_data2 = set(tuple(row) for row in reader)

    # Find differences
    difference_from = testing_data - testing_data2
    difference_to = testing_data2 - testing_data

    # Write difference_from to difference_from.csv
    with open(difference_from_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in difference_from:
            writer.writerow(row)

    # Write difference_to to difference_to.csv
    with open(difference_to_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in difference_to:
            writer.writerow(row)

except Exception as e:
    print(f"An error occurred: {e}")
