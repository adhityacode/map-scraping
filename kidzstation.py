import json
import csv

store_list_datas = []

# Open and read the JSON file
with open('kidzstation_raw.json', 'r') as file:
    data = json.load(file)

datalist = data['data']['data']['dataList']
datalist_mapped = []
for datalist_item in datalist:
    datalist_mapped.append(datalist_item['data'])

# write store list datas into csv file
with open('kidzstation.csv', 'w', newline='') as csvfile:
    fieldnames = datalist_mapped[0].keys()
    print(fieldnames)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(datalist_mapped)

print('write store datas into csv complete')