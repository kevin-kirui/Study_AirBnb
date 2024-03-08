#!/usr/bin/env python3

import json

"""serilize the given data """

data = {
    "name": "kip",
    "graduated": False,
    "age": 32,
    "courses": ["English", "History", "Computer Science", "Coding"],
    "city": "New York",
    "country": "America"
}
# convert to json formatted string
json_string = json.dumps(data)

# Check if the file exists and contains data
file_exists = False
try:
    with open("data.json", "r") as json_file:
        if json_file.read():
            file_exists = True
except FileNotFoundError:
    pass

# If the file exists and contains data, add a comma and newline
if file_exists:
    json_string = ",\n" + json_string
# save the data to a file
with open("data.json", "a") as json_file:
    json_file.write(json_string)

print(json_string)