import os
import csv

# Set the directory containing the CSV files
directory = "inputs/"

# Set the output file name
output_file = "outputs/combined_csvs.csv"

# Initialize a list to store all the rows
combined_rows = []

# Get a list of all CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith(".csv")]

# Loop through each CSV file
for file in csv_files:
    file_path = os.path.join(directory, file)

    # Read the CSV file
    with open(file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skip the header if it's not the first file
        if csv_files.index(file) > 0:
            next(csv_reader)

        # Append each row to the combined_rows list
        for row in csv_reader:
            combined_rows.append(row)

# Write the combined rows to the output file
with open(output_file, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the header
    csv_writer.writerow(combined_rows[0])

    # Write the data rows
    csv_writer.writerows(combined_rows[1:])

print("CSV files combined successfully.")
