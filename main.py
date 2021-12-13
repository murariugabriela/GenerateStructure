import sys
import json
import os


def check_file_writable(file):
    if os.path.exists(file):
        if os.path.isfile(file):
            return os.access(file, os.W_OK)
        else:
            return False
    # target does not exist, check perms on parent dir
    parent_dir = os.path.dirname(file)
    if not parent_dir:
        parent_dir = '.'
    # target is creatable if parent dir is writable
    return os.access(parent_dir, os.W_OK)


def parse_json(json_object: dict, path: str):
    files = []
    for k, v in json_object.items():
        if isinstance(v, dict):
            try:
                os.makedirs(os.path.join(path, k), exist_ok=True)
            except FileExistsError:
                print(f"Error: Directory {os.path.join(path, k)} already exists\n")
            files.append([k, parse_json(v, os.path.join(path, k))])
        else:
            if check_file_writable(os.path.join(path, k)):
                with open(os.path.join(path, k), "w") as file:
                    file.write(v)
            else:
                print("Error: We don't have write access for this file")
            files.append([k, v])
    return files


if __name__ == '__main__':
    print(sys.argv[1], sys.argv[2], "\n", sep="\n")
    if os.path.isfile(sys.argv[1]):
        print("Error: given directory is not a directory\n")
    else:
        if not os.path.isdir(sys.argv[1]):
            print("Error: given directory does not exist... Currently creating it...\n")
            os.mkdir(sys.argv[1])
        try:
            # for a json format of " {'dir': {'file': 'contains'}, 'file': 'contains'}"
            # fisier json ca param
            if os.access(sys.argv[2], os.R_OK):
                with open(sys.argv[2], "r") as f:
                    json_obj = json.loads(f.read())
                    parse_json(json_obj, sys.argv[1])
            else:
                print("Error: We don't have read access for this file")
        except json.JSONDecodeError:
            print("Error: given parameter does not respect json format")
