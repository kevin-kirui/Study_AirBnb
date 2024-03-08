#!/usr/bin/env python3

import json

"""Deserialization of data"""

# Load from the JSON file
with open("data.json", "r") as json_file:
    # Read the contents of the file
    json_data = json_file.read()

    # Split the JSON data into individual JSON objects
    json_objects = json_data.split("\n")

    # Iterate through each JSON object
    for json_obj in json_objects:
        # Skip empty lines
        if not json_obj.strip():
            continue
        
        # Deserialize the JSON object
        data = json.loads(json_obj)

        # Print the deserialized data
        print(data["name"])
        print(data["graduated"])
        print(data["city"])
        print(data["country"])
        print(data["courses"])
        print(data)
