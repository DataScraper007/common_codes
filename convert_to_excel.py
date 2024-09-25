import pandas as pd
import mysql.connector


def convert_to_excel(database, table, columns, filename):
    
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='actowiz',
        database= database
    )
    
    data = pd.read_sql(f'SELECT * from {table}', conn)
    # columns = columns.split(' ')
    # if columns:
    #     data = data.drop(columns, axis=1)
    
    data.to_excel(f'{filename}.xlsx', index=False)


if __name__ == '__main__':
    convert_to_excel('qcg', 'swg_new_links','', 'Swiggy updated')