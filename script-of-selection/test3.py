import csv

# File paths
testing_data_path = 'testing_data.csv'
test_files_path = 'test_files.csv'

try:
    # Read rows from testing_data.csv
    with open(testing_data_path, 'r', encoding='utf-8') as file:
        testing_data_reader = csv.reader(file)
        testing_data_rows = [row for row in testing_data_reader]

    # Read rows from test_files.csv
    with open(test_files_path, 'r', encoding='utf-8') as file:
        test_files_reader = csv.reader(file)
        test_files_rows = [row for row in test_files_reader]

    # Compare rows
    for test_row in testing_data_rows:
        if test_row in test_files_rows:
            # save the row to the csv file "found.csv"
            with open('found.csv', 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(test_row)
        else:
            # save the row to the csv file "not_found.csv"
            with open('not_found.csv', 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(test_row)

except Exception as e:
    print(f"An error occurred: {e}")
