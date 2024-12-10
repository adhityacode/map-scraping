import requests
import csv

# 
curpage = 1
store_list_datas = []
stop = False

url = 'https://www.planetsports.asia/storelocator/index/loadstore/'
headers = {
    'x-requested-with': 'XMLHttpRequest',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

# loop through all the pagination pages and store store informations inside list
while stop == False:
    payload = "curPage="+ str(curpage)
    r = requests.post(url=url, headers=headers, data=payload)

    response_json = r.json()
    storesjson = response_json['storesjson']
    num_store = response_json['num_store']

    for store in storesjson:
        store_list_datas.append({
            "store_name": store['store_name'],
            "store_contact": store['phone'],
            "full_address": store['address'],
            "full_long_lat": store['longitude']+','+store['latitude'],
            "longitude": store['longitude'],
            "latitude": store['latitude'],
        })
    curpage += 1
    if(len(store_list_datas) >= num_store):
        stop = True

print(store_list_datas)

# write store list datas into csv file
with open('planetsports.csv', 'w', newline='') as csvfile:
    fieldnames = ['store_name', 'store_contact', 'full_address', 'full_long_lat','longitude', 'latitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(store_list_datas)

print('write store datas into csv complete')