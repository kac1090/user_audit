import pandas as pd


def load_data():
    employees_df = pd.read_csv('../data/employees.csv')
    system_access_df = pd.read_csv('../data/system_access.csv')
    
    return employees_df, system_access_df


def clean_id(system_access_df):
    system_access_df['id'] = 'EMP' + system_access_df['id'].astype(str).str.zfill(6)
    
    return system_access_df
    

def join_data(employees_df, system_access_df):
    return employees_df.merge(system_access_df, left_on='employee_number', right_on='id', how='left')

def null_data(master_df):
    return master_df[master_df.isnull().any(axis=1)]