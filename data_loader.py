import csv

EXPECTED_COLUMNS = ['Name', 'Value', 'Status']

def load_data(file_path):
    data_list = []
    try:
        with open(file_path, mode='r', newline='')
            reader = csv.reader(f)

            next(reader)

            for row in reader:
                if not len(row) == len(EXPECTED_COLUMNS):
                    print(f"Skipping malformed row: {row}")
                    continue

                if is_valid_entry(row):
                    data_list.append(row)

    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

    return data_list