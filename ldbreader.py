#!/usr/bin/python3

import plyvel
from os import path
import json
import sys


# Путь к папке с файлами .ldb

try:
    db_path = sys.argv[1]
except:
    sys.stderr.write("Укажите путь к БД!\n")
    sys.exit(1)
    

# Открыть БД
try:
    db = plyvel.DB(db_path)
except IOError:
    sys.exit(1)


data = {}
# Преобразование БД в файл .json
with open('RESULT.json', 'w+') as f:
    for k, v in db:
        key = k.decode('utf-8',errors='ignore')
        value = v.decode('utf-8',errors='ignore')
        value_json = json.loads(value)
        data[f'{key}'] = value_json
        data_json_string = json.dumps(data, indent=4)

    f.write(data_json_string)

f.close()   
    
