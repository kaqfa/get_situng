import requests
import csv
from datetime import datetime

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://pemilu2019.kpu.go.id/static/json/wilayah'
t_url = 'https://pemilu2019.kpu.go.id/static/json/hhcw/ppwp'

def get_subs(super_url):
    res  = requests.get(super_url, verify=False)
    djson = res.json()
    data = []
    for key, value in djson.items():
        data.append((key, value['nama']))
        
    return data

def check_tps(tps_data):
    djson  = requests.get(tps_data['url'], verify=False).json()
    
    if djson == None:
        return None
    
    data = {'tps_id': tps_data['tps_id'], 'images': djson['images'], 
            'pas_01': djson['chart']['21'], 'pas_02': djson['chart']['22'],
            'sah': djson['suara_sah'], 'tdk_sah': djson['suara_tidak_sah'],
            'total': djson['suara_total']}
    
    if (data['pas_01'] + data['pas_02'] != data['sah']) or \
       (data['sah'] + data['tdk_sah'] != data['total']):
        data['status'] = 'anomali_1'
    else:
        data['status'] = 'normal'
    
    return data

def pack_to_csv(csv_data):
    header = ['tps_id', 'images', 'pas_01', 'pas_02', 'sah', 'tdk_sah', 'total', 'status']
    now = datetime.now()
    date_time = now.strftime("%m_%d_%Y__%H_%M_%S")
    with open('dkpu_'+date_time+'.csv', 'w') as writeFile:
        writer = csv.DictWriter(writeFile, fieldnames=header)
        writer.writeheader()
        for data in csv_data:
            writer.writerow(data)
            
    writeFile.close()
    
## ====== Ready, set, action ======>

provs = get_subs(url+'/0.json')

area = []

for prov in provs:
    """ build data list TPS di semua wilayah terlebih dahulu
    """
    print('building area data')
    prov_url = '{}/{}.json'.format(url,prov[0])
    cities = get_subs(prov_url)
    for city in cities:
        city_url = '{}/{}/{}.json'.format(url,prov[0],city[0])
        kecs = get_subs(city_url)
        for kec in kecs:
            kec_url = '{}/{}/{}/{}.json'.format(url,prov[0],city[0],kec[0])
            kels = get_subs(kec_url)
            for kel in kels:
                kel_url = '{}/{}/{}/{}/{}.json'.format(url,prov[0],city[0],kec[0],kel[0])
                tpss = get_subs(kel_url)
                for tps in tpss:
                    tps_url = kel_url = '{}/{}/{}/{}/{}/{}.json'.format(t_url,prov[0],city[0],kec[0],kel[0],tps[0])
                    tps_data = {'url': tps_url, 'prov': prov[1], 'city': city[1], 
                                'kec': kec[1], 'kel': kel[1], 'tps': tps[1], 'tps_id': tps[0]}
                    area.append(tps_data)
                    print('.', end=' ')

print('\ntime to harvest data')
while True:
	csv_data = []
	for tps in area:
		res_check = check_tps(tps)
		if res_check is not None:
			csv_data.append(res_check)
			print('.', end=' ')
    
	print('\nwrite new csv data')
	pack_to_csv(csv_data)
	print('finish writing csv and restart harvesting')
