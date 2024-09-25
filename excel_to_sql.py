import pandas as pd
from sqlalchemy import create_engine

# Database connection string (using SQLite for this example)
DATABASE_URL = "mysql+pymysql://root:actowiz@localhost:3306/qcg"  # Change this to your database URL

# Excel file path
EXCEL_FILE_PATH = r"C:\Users\Admin\Downloads\Swiggy_updated.xlsx"  # Replace with the path to your Excel file

# Table name and SQLAlchemy metadata
TABLE_NAME = "swg_new_links"

client = create_engine(DATABASE_URL)
df = pd.read_excel(EXCEL_FILE_PATH)
df.to_sql(TABLE_NAME, client)

