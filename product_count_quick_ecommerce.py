import pymysql
import pandas as pd

# Database connection configuration
db_host = 'localhost'
db_user = 'root'
db_password = 'actowiz'
db_port = 3306
db_database = 'qcg'



def fetch_data(date):
    # SQL query to integrate results
    query = f"""
    SELECT
        pincode,
        SUM(dmt) AS dmt,
        SUM(jmt) AS jmt,
        SUM(blk) AS blk,
        SUM(bb) AS bb,
        SUM(amz) AS amz
    FROM (
        SELECT pincode, COUNT(name) AS dmt, 0 AS jmt, 0 AS blk, 0 AS bb, 0 AS amz
        FROM dmt_{date}
        GROUP BY pincode
        UNION ALL
        SELECT pincode, 0 AS dmt, COUNT(name) AS jmt, 0 AS blk, 0 AS bb, 0 AS amz
        FROM jmt_{date}
        GROUP BY pincode
        UNION ALL
        SELECT pincode, 0 AS dmt, 0 AS jmt, COUNT(name) AS blk, 0 AS bb, 0 AS amz
        FROM blk_{date}
        GROUP BY pincode
        UNION ALL
        SELECT pincode, 0 AS dmt, 0 AS jmt, 0 AS blk, COUNT(name) AS bb, 0 AS amz
        FROM bb_{date}
        GROUP BY pincode
        UNION ALL
        SELECT pincode, 0 AS dmt, 0 AS jmt, 0 AS blk, 0 AS bb, COUNT(name) AS amz
        FROM amz_{date}
        GROUP BY pincode
    ) AS combined
    GROUP BY pincode;

    """

    # Connect to the database
    connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_database)
    try:
        # Execute the query
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
    finally:
        connection.close()

    return results


def save_to_excel(data, filename):
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['pincode', 'dmt', 'jmt', 'blk', 'bb', 'amz'])

    # Save the DataFrame to an Excel file
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Summary')


if __name__ == "__main__":

    date = input("Enter date: (eg: 20240810): " )
    # Fetch data from the database
    data = fetch_data(date)

    # Define the output Excel file name
    output_file = f'product_count_summary_{date}.xlsx'

    # Save the data to an Excel file
    save_to_excel(data, output_file)

    print(f"Data has been successfully saved to {output_file}")
