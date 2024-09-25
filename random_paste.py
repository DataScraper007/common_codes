import os
import random
import shutil
from datetime import datetime


def modify_time(folder_path):
    current_time = datetime.now().timestamp()
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            os.utime(file_path, (current_time, current_time))
            print(f"Modified date of '{file_path}' has been updated to the current time.")


def copy_random_files_from_folders(source_folders, dest_folder):
    all_files = []

    src_file_count = len(os.listdir(source_folders[0]))

    for folder in source_folders:
        folder_files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        random.shuffle(folder_files)
        all_files.extend([(folder, file) for file in folder_files])
    random.shuffle(all_files)

    all_files = all_files

    for src_folder, random_file in all_files:
        src_file_path = os.path.join(src_folder, random_file)
        dest_file_path = os.path.join(dest_folder, random_file)
        dest_file_count = len(os.listdir(dest_folder))
        if src_file_count <= dest_file_count:
            return

        if os.path.exists(dest_file_path):
            os.remove(dest_file_path)
            print(f"Deleted existing file: {dest_file_path}")

        shutil.copy(src_file_path, dest_file_path)
        print(f"Copied {random_file} from {src_folder} to {dest_folder}")


if __name__ == '__main__':
    source_folders = [
        r"C:\Users\Admin\PycharmProjects\common_code\csvs",
        r"C:\Users\Admin\PycharmProjects\common_code\csvs_",
    ]

    dest_folder = r"C:\Users\Admin\PycharmProjects\common_code\output_folder"

    copy_random_files_from_folders(source_folders, dest_folder)

    print("Files have been copied successfully..")

    modify_time(dest_folder)

    print("Modified time updated successfully..")
