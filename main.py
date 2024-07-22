import logging
import os
from collections import defaultdict


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def categorize_files_by_type(folder_path):
    dic = defaultdict(list)

    if not os.path.isdir(folder_path):
        logging.error("There's no such path")
        return dic

    logging.info(f"Starting to categorize files in directory: {folder_path}")
    try:
        for root, dirs, files in os.walk(folder_path):
            logging.info(f"Processing directory: {root}")
            for file in files:
                extension = os.path.splitext(file)[1]
                full_path = os.path.join(root, file)
                if extension:
                    dic[extension].append(full_path)
                else:
                    dic[''].append(os.path.join(root, file))
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    logging.info("Finished categorizing files")
    return dic


result = categorize_files_by_type("/Users/arapbaysungat/Documents")

print(dict(result))
