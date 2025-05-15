import csv
import json
import requests

# def writ_json(data, filename='student.json'):
#     with open (filename, 'w') as f:
#         json.dump(data, f, indent=4)
#
#
# with open ('student.json') as json_file:
#     data = json.load(json_file)
#     temp = data('names')
#     y = {"firstname": "Joe", "age": 40}
#     temp.append(y)
#
# writ_json(data)


# convert from json to csv

# with open('student.json', 'r') as f:
#     data = json.load(f)
#     names = data["names"]
#
# with open("student.csv", "w") as csv_f:
#     fieldnames = names[0].keys()
#     writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
#     writer.writeheader()
#     for name in names:
#         writer.writerow(name)


# hw_14 2

r = requests.get('https://openweathermap.org/')

print(r.text)
