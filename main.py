import sys
import json


def parse_json(json_object: dict, path: str):
    files = []
    for k, v in json_object.items():
        if isinstance(v, dict):
            files.append([k, parse_json(v, path + "\\" + k)])
        else:
            print(path, k, v)
            files.append([k, v])
    return files


if __name__ == '__main__':
    print(sys.argv[1], sys.argv[2], sep="\n")
    json_obj = json.loads(sys.argv[2])
    parse_json(json_obj, sys.argv[1])
