import csv

import pandas as pd


def read_employee_data(data):
    """
    Reads employee data from a CSV file and returns a pandas DataFrame.

    filepath_or_buffer: A string representing the file path or a file-like object of the CSV data.
    quotechar: A character used to denote quotes in the CSV file.
    header: An integer or list of integers representing the row number(s) to use as the column names.
    sep: A regular expression pattern used to separate fields in the CSV file.
    skipinitialspace: A boolean value indicating whether to skip leading spaces in the fields.
    quoting: An integer constant representing the CSV quoting style.
    engine: The parsing engine to use.

    After reading the CSV data, we replace any spaces in the column names with underscores using the str.replace method
    on the columns attribute of the DataFrame.

    :param data: A string representing the file path or a file-like object of the CSV data.
    :return: A pandas DataFrame containing the employee data.
    """

    # Read employee data from a CSV file using pandas' read_csv function
    employee_df = pd.read_csv(filepath_or_buffer=data, header=0, sep='|', index_col=False, quoting=csv.QUOTE_NONE)
    # Replace any spaces in the column names with underscores for consistency and ease of use
    # Also having spaces in column names is a bad DB practice and may throw errors for future steps
    employee_df.columns = employee_df.columns.str.replace(' ', '_')
    # Remove double quotes in order to have clean data in MySQL DB
    remove_quotes_df = employee_df.apply(lambda s: s.str.replace('"', ""))
    return remove_quotes_df


def write_employee_data(data):
    pass
