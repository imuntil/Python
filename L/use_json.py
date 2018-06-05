import json


def write_json():
    """write something to json"""
    filename = 'pp.json'
    with open(filename, 'a') as f_obj:
        json.dump({
            'numbers': [1, 2, 3, 4, 5]
        }, f_obj)


def read_json():
    """read something from json"""
    filename = 'pp.json'
    with open(filename) as f_obj:
        content = json.load(f_obj)
        print(type(content))
        print(content)


# write_json()
read_json()
