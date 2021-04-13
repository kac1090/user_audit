import pandas as pd


def load_data():
    employees_df = pd.read_csv('../data/employees.csv')
    system_access_df = pd.read_csv('../data/system_access.csv')
    
    return employees_df, system_access_df
    
              