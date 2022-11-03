import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # create a dict
    data_dict = {}

    # open a csv file 
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csvreader = csv.DictReader(csv_file)

        # convert each row into a dictionary and adding to the data_dict variable
        for rows in csvreader:
            key = rows['Serial Number']
            data_dict[key] = rows

    # open a json file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_obj = json.dumps(data_dict, indent=4)
        json_file.write(json_obj)

# input to take the absolute url location of the path
csv_file_path = input('Enter the absolute path of the CSV file: ')
json_file_path = input('Enter the absolute path of the JSON file: ')

print('working on it...')

csv_to_json(csv_file_path, json_file_path)
