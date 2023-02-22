import requests
import json
headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer 4-9q86gRe6JfwE_sI0FkDz_H4ca9U2ye',
}


# for i in range(1, 9):
response = requests.get(f'https://student.tersu.uz/rest/v1/data/employee-list?type=teacher&page=1&limit=200',
                            headers=headers)
data_all = response.json()

for j in data_all['data']['items']:
    print(str(j['full_name']))