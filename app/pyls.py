import json
import os
import sys
from datetime import datetime
from utils import human_readable_size, parse_epoch_time

class PyLS:
    def __init__(self, json_file='structure.json'):
        with open(json_file) as f:
            self.structure = json.load(f)
    
    def list_files(self, show_hidden=False):
        contents = self.structure.get('contents', [])
        for item in contents:
            if not show_hidden and item['name'].startswith('.'):
                continue
            print(item['name'])

    def list_files_detailed(self, reverse=False, sort_by_time=False):
        contents = self.structure.get('contents', [])
        if sort_by_time:
            contents.sort(key=lambda x: x['time_modified'], reverse=True)

        if reverse:
            contents = reversed(contents)

        for item in contents:
            permissions = item['permissions']
            size = human_readable_size(item['size'])
            time_modified = parse_epoch_time(item['time_modified'])
            print(f"{permissions} {size} {time_modified} {item['name']}")

# Command-line handling
if __name__ == '__main__':
    pyls = PyLS()

    # Parsing command-line arguments (simplified)
    if '-A' in sys.argv:
        pyls.list_files(show_hidden=True)
    elif '-l' in sys.argv:
        reverse = '-r' in sys.argv
        sort_by_time = '-t' in sys.argv
        pyls.list_files_detailed(reverse=reverse, sort_by_time=sort_by_time)
    else:
        pyls.list_files()
