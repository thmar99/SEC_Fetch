import pandas as pd
import re

def remChar(cell):
    '''remove specific strings mixed in with cells, and all subsequent characters''' 
    if isinstance(cell, str):
        return re.sub(r'[^0-9.]', '', cell)  # Remove non-numeric characters
    return cell

def CleanSheet(DataFrame):   
    #Remove footer notes
    null_val = lambda row : True if str(row[0])=="" or str(row[0])=='nan' else False
    for index,row in DataFrame.iterrows():
        if "[" in str(row[0]) or null_val(row): DataFrame.drop(index,inplace=True)

    #drop empty columns
    DataFrame.dropna(how='all',axis=1,inplace=True)
    #DataFrame.to_csv('after_empty_cols.csv')

    #drop columns that contain square brackets and integers between
    pattern = r'\[\d+\]'
    # Identify columns containing the specified pattern
    columns_to_drop = [col for col in DataFrame.columns if any(DataFrame[col].apply(lambda x: re.search(pattern, str(x))))]
    # strip non-numerical characters in the columns
    df_cleaned = DataFrame.drop(columns=columns_to_drop)
    df_clean = df_cleaned.applymap(remChar)
    df_cleaned.to_csv('ba_test_result.csv',index=False)

    return df_clean

sheet = pd.read_csv('ba_test_table.csv')
sheet.reset_index(drop=True,inplace=True)
res = CleanSheet(sheet)
