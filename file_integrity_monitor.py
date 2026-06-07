import hashlib
import json


def hash_digest(filename: str):
    hasher = hashlib.sha256()
    try:
        with open(f'files/{filename}', 'rb') as file:
            hasher.update(file.read())
        return hasher.hexdigest()
    except FileNotFoundError:
        print('File Not Found!!')

def baseline_check(file: dict, filename:str):
    value = False
    try:
        with open('baseline.json', 'r') as f:
            data = json.load(f)
        if filename not in data.keys():
            value = True
    except FileNotFoundError:
        value = True
    return value
        
def baseline(file: dict):
    try:
        with open('baseline.json', 'r') as f:
            data = json.load(f)
        data.update(file)
    except FileNotFoundError:
        data = file
    with open('baseline.json', 'w') as f:
        json.dump(data, f, indent=4)
    
def integrity_check(file: dict, filename: str):
    value = False
    with open('baseline.json', 'r') as f:
        data = json.load(f)
    if file[filename] == data[filename]:
        value = True
    return value

if __name__ == "__main__":
    file = dict()
    filename = input('What is filename: ')
    hex_digest = hash_digest(filename)
    file = {filename: hex_digest}
    if baseline_check(file, filename):
        baseline(file)
    else:   
        if integrity_check(file, filename):
            print('File is the same')
        else:
            print('Something Wrong with file')
    print(f'Hash Digest: {hex_digest}')
