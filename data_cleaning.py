import time
from datetime import datetime

import pandas as pd
import numpy as np

start_time = time.time()

# Load the Excel file
filename = r"C:\Users\Admin\PycharmProjects\common_code\Comp_Raw_Data_20240910.xlsx"
output_file_name = "Comp_Raw_Data_20240910_copy.xlsx"

delivery_date = datetime.today().strftime("%Y%m%d")

df1 = pd.read_excel(filename, sheet_name=0, engine='calamine')
print(1)
df2 = pd.read_excel(filename, sheet_name=1, engine='calamine')
print(2)

sheet_names = pd.ExcelFile(filename).sheet_names
# Apply the cleaning operation across the entire DataFrame
df1 = df1.apply(lambda x: x.str.strip().replace('', np.nan) if x.dtype == "object" else x)

# Apply the cleaning operation across the entire DataFrame
df2 = df2.apply(lambda x: x.str.strip().replace('', np.nan) if x.dtype == "object" else x)

# Case 0: NAME is N/A
case_0 = df1['name'] == 'N/A'
df1 = df1[~case_0]

# Case 1: URL is blank
case_1 = df1['url'].isnull()
df1.loc[case_1, ['name', 'availability', 'price', 'discount', 'mrp']] = np.nan

# Case 2: URL is not blank but name is blank
case_2 = df1['url'].notnull() & df1['name'].isnull()
df1.loc[case_2, ['availability', 'price', 'discount', 'mrp']] = np.nan

# Case 3: URL is not blank, name is not blank, but availability is blank
case_3 = df1['url'].notnull() & df1['name'].notnull() & df1['availability'].isnull()
df1.loc[case_3, ['price', 'discount', 'mrp']] = np.nan

# Case 4: URL is not blank, name is not blank, availability is 1, but price is blank
case_4 = df1['url'].notnull() & df1['name'].notnull() & (df1['availability'] == 1.0) & df1['price'].isnull()
df1.loc[case_4, ['price', 'discount', 'mrp', 'availability']] = [np.nan, np.nan, np.nan, 0]

# Case 5: URL is not blank, name is not blank, availability is not blank, price is not blank, but mrp is blank
case_5 = df1['url'].notnull() & df1['name'].notnull() & df1['availability'].notnull() & df1['price'].notnull() & df1[
    'mrp'].isnull()
df1.loc[case_5, 'discount'] = np.nan

# Same for df2

# Case 0: NAME is N/A
case_0 = df2['name'] == 'N/A'
df2 = df2[~case_0]

# Case 1: URL is blank
case_1 = df2['url'].isnull()
df2.loc[case_1, ['name', 'availability', 'price', 'discount', 'mrp']] = np.nan

# Case 2: URL is not blank but name is blank
case_2 = df2['url'].notnull() & df2['name'].isnull()
df2.loc[case_2, ['availability', 'price', 'discount', 'mrp']] = np.nan

# Case 3: URL is not blank, name is not blank, but availability is blank
case_3 = df2['url'].notnull() & df2['name'].notnull() & df2['availability'].isnull()
df2.loc[case_3, ['price', 'discount', 'mrp']] = np.nan

# Case 4: URL is not blank, name is not blank, availability is 1, but price is blank
case_4 = df2['url'].notnull() & df2['name'].notnull() & (df2['availability'] == 1.0) & df2['price'].isnull()
df2.loc[case_4, ['price', 'discount', 'mrp', 'availability']] = [np.nan, np.nan, np.nan, 0]

# Case 5: URL is not blank, name is not blank, availability is not blank, price is not blank, but mrp is blank
case_5 = df2['url'].notnull() & df2['name'].notnull() & df2['availability'].notnull() & df2['price'].notnull() & df2[
    'mrp'].isnull()
df2.loc[case_5, 'discount'] = np.nan

with pd.ExcelWriter(output_file_name, engine='openpyxl') as writer:
    df1.to_excel(writer, index=False, sheet_name=f"Comp data 1 - Value Players_{delivery_date}")
    df2.to_excel(writer, index=False, sheet_name=f"Comp data 2 - Quick Commerce_{delivery_date}")
