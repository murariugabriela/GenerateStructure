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
                print(f"Error: file {path}\\{k} already exists")
            files.append([k, parse_json(v, path + "\\" + k)])
        else:
            f = open(path + "\\" + k, "w")
            f.write(v)
            f.close()
            files.append([k, v])
    return files


if __name__ == '__main__':
    print(sys.argv[1], sys.argv[2], sep="\n")
    json_obj = json.loads(sys.argv[2])
    parse_json(json_obj, sys.argv[1])
