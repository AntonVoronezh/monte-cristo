import json


def update_json_file(file_name, part, key, new_value):
    json_file = open(file_name, "r")  # Open the JSON file for reading
    data = json.load(json_file)  # Read the JSON into the buffer
    json_file.close()  # Close the JSON file

    data[part][key] = new_value

    ## Save our changes to JSON file
    json_file = open(file_name, "w+")
    json_file.write(json.dumps(data, indent=4))
    json_file.close()