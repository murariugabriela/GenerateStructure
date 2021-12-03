import sys
import json
import os


def parse_json(json_object: dict, path: str):
    files = []
    for k, v in json_object.items():
        if isinstance(v, dict):
            try:
                os.mkdir(path + "\\" + k)
            except FileExistsError:
                print(f"Error: Directory {path}\\{k} already exists\n")
            files.append([k, parse_json(v, path + "\\" + k)])
        else:
            f = open(path + "\\" + k, "w")
            f.write(v)
            f.close()
            files.append([k, v])
    return files


if __name__ == '__main__':
    print(sys.argv[1], sys.argv[2], "\n", sep="\n")
    if os.path.isfile(sys.argv[1]):
        print("Error: given directory is not a directory\n")
    else:
        if not os.path.isdir(sys.argv[1]):
            print("Error: given directory does exist... Currently creating it...\n")
            os.mkdir(sys.argv[1])
        try:
            # for a json format of " {'dir': {'file': 'contains'}, 'file': 'contains'}"
            json_obj = json.loads(sys.argv[2].replace("'", "\""))
            parse_json(json_obj, sys.argv[1])
        except json.JSONDecodeError:
            print("Error: given parameter does not respect json format")
