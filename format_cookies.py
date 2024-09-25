import pandas as pd
import json


def cookies_to_json(cookie_string):
    cookies = cookie_string.split("; ")
    cookie_dict = {}
    for cookie in cookies:
        key, value = cookie.split("=", 1)
        cookie_dict[key] = value
    return json.dumps(cookie_dict, indent=4)


if __name__ == '__main__':

    df = pd.read_excel(r"C:\Users\Admin\Downloads\jio sim.xlsx", sheet_name="meesho cookie", engine='calamine')
    # print(pd.ExcelFile(r'C:\Users\Admin\Downloads\jio sim.xlsx').sheet_names)
    print(df.columns.tolist())

    columns = [pd.Timestamp('2024-09-06 00:00:00'), pd.Timestamp('2024-06-08 00:00:00'),
               pd.Timestamp('2024-09-09 00:00:00'), pd.Timestamp('2024-11-09 00:00:00'),
               pd.Timestamp('2024-12-09 00:00:00'), '13-09-2024']

    for column in columns:
        cookies = df[column].dropna()
        print(len(cookies))
        c = []
        for cookie_string in cookies:
            json_cookies = cookies_to_json(cookie_string)
            if isinstance(json_cookies, str):
                json_cookies = json.loads(json_cookies)
            c.append(json_cookies)
        with open(f"meesho_cookie_{column}.json", 'w') as json_file:
            json.dump(c, json_file, indent=4)

#
# import json
#
# l = [
#     r'C:\Users\Admin\PycharmProjects\common_code\cookies_06_09_2024.json',
#     r'C:\Users\Admin\PycharmProjects\common_code\cookies_08_09_2024.json',
#     r'C:\Users\Admin\PycharmProjects\common_code\cookies_12_09_2024.json',
#     r'C:\Users\Admin\PycharmProjects\common_code\cookies_13_09_2024.json'
# ]
#
# m = []
#
# for file_path in l:
#     with open(file_path, 'r') as file:
#         cookies = json.load(file)
#         m.extend(cookies)
# # Write the merged list of cookies to a new JSON file
# with open("meesho_cookies.json", 'w') as json_file:
#     json.dump(m, json_file, indent=4)
