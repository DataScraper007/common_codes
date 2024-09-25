import pandas as pd
import glob
import os

csv_directory = r'C:\Users\Admin\PycharmProjects\common_code\csvs'

csv_files = glob.glob(os.path.join(csv_directory, '*.csv'))

# unique_names = set()
#
# for file in csv_files:
#     df = pd.read_csv(file)
#     if 'Name' in df.columns:
#         unique_names.update(df['Name'].dropna().unique())
#         print(f"{file} Done.")
#
# unique_names_df = pd.DataFrame(list(unique_names), columns=['Name'])
#
# excel_output_path = 'top_computer_and_electronics_stores.xlsx'
#
# unique_names_df.to_excel(excel_output_path, index=False)
#
# print(f"Unique names have been written to {excel_output_path}")

dfs = []

for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

unique_df = merged_df.drop_duplicates(subset='Provider', keep='first')

excel_output_path = 'provider_names.xlsx'

unique_df.to_excel(excel_output_path, index=False)
