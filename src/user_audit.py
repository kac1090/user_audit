import pandas as pd


def load_data():
    employees_df = pd.read_csv('../data/employees.csv')
    system_access_df = pd.read_csv('../data/system_access.csv')
    
    return employees_df, system_access_df


def clean_id(system_access_df):
    system_access_df['id'] = 'EMP' + system_access_df['id'].astype(str).str.zfill(6)
    
    return system_access_df
    