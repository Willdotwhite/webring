#!/usr/bin/env python3
import json
import random
from datetime import datetime

data_file_path = './../../data.json'


def shuffle_data_array():
    # Generate a seed that will order list deterministically
    seed: str = datetime.today().strftime('%Y%m%d')
    with open(data_file_path, 'r+') as file:
        # Load current list from file and shuffle (in place)
        webring_list: list[dict[str, str]] = json.loads(file.read())
        random.Random(int(seed)).shuffle(webring_list)

        # Overwrite existing file contents with new list
        # (Move file pointer to position 0, write new list, bin off everything else)
        # This means we don't need to open the file a second time for writing
        file.seek(0)
        file.write(json.dumps(webring_list, indent=4, ensure_ascii=False))
        file.truncate()


if __name__ == "__main__":
    shuffle_data_array()
