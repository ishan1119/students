import csv

import pandas as pd


def read_employee_data(data):
    """

    :param file:
    :return:
    """
    employee_df = pd.read_csv(filepath_or_buffer=data, quotechar='"', header=0, sep=',\s*', skipinitialspace=True,
                              quoting=csv.QUOTE_ALL, engine='python')
    employee_df.columns = employee_df.columns.str.replace(' ', '_')
    return employee_df


def write_employee_data(data):
    pass
