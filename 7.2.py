import requests
import pandas as pd
page_number=0
search_str="qlik"
area_str="1"
url="https://api.hh.ru/vacancies"
param={
    "text":search_str,
    "area":area_str,
    "page":page_number
}
response=requests.get(url,param)
data=response.json()
dict_data={}
dict_number=0
for i in range(0,data['pages']):
    param_cycle={
       "text":search_str,
       "area":area_str,
       "page":i
    }
    response_cycle=requests.get(url,param_cycle)
    print("Запрос №"+str(i))
    result=dict(response_cycle.json())
    result=result['items']
    for y in range(0,len(result)-1):
        dict_data[dict_number]={
            'id':result[y]['id'],
            'premium':result[y]['premium'],
            'name':result[y]['name'],
            'department':result[y]['department'],
            'has_test':result[y]['has_test'],
            'area_name':result[y]['area']['name'],
            'salary':result[y]['salary'],
            'type_name':result[y]['type']['name'],
            'snippet_requirement':result[y]['snippet']['requirement']
        }
        dict_number=dict_number+1 
    print("=================================")
print(dict_data[0])
