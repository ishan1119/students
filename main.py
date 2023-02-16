from src.employee import read_employee_data
from utils.constants import employee_path

if __name__ == '__main__':
    print(read_employee_data(data=employee_path))
