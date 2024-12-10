import json
import csv

store_list_datas = []

# Open and read the JSON file
with open('stevemadden_raw.json', 'r') as file:
    data = json.load(file)

datalist = data['stores']
datalist_mapped = []
for i in datalist:
    datalist_mapped.append({
        'store_id': i['store_id'],
        'lng': i['lng'],
        'lat': i['lat'],
        'website': i['website'],
        'name': i['name'],
        'postal_zip': i['postal_zip'],
        'name': i['name'],
        'address': i['address'],
        'address2': i['address2'],
        'hours': i['hours'],
        'city': i['store_id'],
        'prov_state': i['prov_state'],
        'country': i['country'],
        'phone': i['phone'],
        'email': i['email'],
        'fax': i['fax'],
    })

# write store list datas into csv file
with open('stevemadden.csv', 'w', newline='') as csvfile:
    fieldnames = datalist_mapped[0].keys()
    print(fieldnames)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(datalist_mapped)

print('write store datas into csv complete')