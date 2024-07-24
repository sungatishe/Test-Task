import logging
import os
from collections import defaultdict
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# This function categorizes files based on their extensions within a specified directory and its subdirectories.
# It can optionally filter files by their modification dates, only including those modified within the specified
# date range.
def categorize_files_by_type(folder_path, min_time=None, max_time=None):
    dic = defaultdict(list)

    if not os.path.isdir(folder_path):
        logging.error("There's no such path")
        return dic

    logging.info(f"Start in directory: {folder_path}")

    min_mtime = convert_date(min_time) if min_time else None
    max_mtime = convert_date(max_time) if max_time else None
    try:
        for root, dirs, files in os.walk(folder_path):
            logging.info(f"Processing directory: {root}")
            for file in files:
                full_path = os.path.join(root, file)
                try:
                    stat = os.stat(full_path)
                except OSError:
                    logging.warning(f"Could not access file: {full_path}")
                    continue

                if min_mtime is not None and stat.st_mtime < min_mtime:
                    continue
                if max_mtime is not None and stat.st_mtime > max_mtime:
                    continue

                extension = os.path.splitext(file)[1]
                if extension:
                    dic[extension].append(full_path)
                else:
                    dic[''].append(os.path.join(root, file))
    except Exception as e:
        logging.error(f"Error occurred: {e}")

    logging.info("Finished")
    return dic


# Converts a date string in 'YYYYMMDD' format to a Unix timestamp.
def convert_date(date_str):
    try:
        return int(datetime.strptime(date_str, "%Y%m%d").timestamp())
    except ValueError:
        logging.error(f"Invalid date format: {date_str}. Expected format is 'YYYYMMDD'.")
        return None


# Enter your path (e.g. "/Users/User/Documents")
path = "/Users/"

result = categorize_files_by_type(
    path,
    min_time='20210101',
    max_time='20240101'
)

print(dict(result))
