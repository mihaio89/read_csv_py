import csv
from itertools import islice
import logging

from constants import CSV_FILE, TXT_FILE, LOG_FILE , LOG_FORMAT, LOG_FORMAT_DATE

input_file  = CSV_FILE
output_file = TXT_FILE

log_file = 'logfile.log'  # Specify the log file path

def configure_logging():
    # Configure logging to log messages to both console and file
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT, datefmt=LOG_FORMAT_DATE,
        handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()]
    )

def init():
    configure_logging()

def process_file():

    row_count = 0
    
    with open(input_file, 'r') as file:
        csv_reader = csv.reader(file)

        # Skip the header row
        next(csv_reader)

        with open(output_file, 'w', newline='') as txt_output:
            # Iterate through each row in the CSV file
            for row in csv_reader:
                # Convert the row to a string and write it to the text file
                txt_output.write(','.join(row) + '\n')
                row_count += 1

    # Post-process the file to replace '\r\n' with '\n'
    with open(output_file, 'r') as file:
        content = file.read()

    with open(output_file, 'w', newline='') as file:
        file.write(content.replace('\r\n', '\n'))

    logger.info(f'{row_count} rows written to {output_file} from {input_file}')

def print_rows(file, n):
    print(f'printing the first {n} rows from {file}')
    with open(file, 'r') as file:
        csv_reader = csv.reader(file)

        # Use itertools.islice to iterate over the first n rows
        for row in islice(csv_reader, n):
            print(row)


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    init()
    print_rows(CSV_FILE, 3)
    process_file()
    print_rows(TXT_FILE, 3)
