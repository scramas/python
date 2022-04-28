import requests
import pandas as pd
import xml.etree.ElementTree as et
v_date='10.06.2021'
url='https://www.cbr.ru/scripts/XML_daily.asp'
params={
    'date_req':v_date
}
response=requests.get(url,params)
tree=et.ElementTree(et.fromstring(response.text))
root=tree.getroot()
df_cols=["date","numcode","charcode","nominal","name","value"]
rows=[]
for node in root:
    s_numcode=node.find("NumCode").text if node is not None else None
    s_charcode=node.find("CharCode").text if node is not None else None
    s_nominal=node.find("Nominal").text if node is not None else None
    s_name=node.find("Name").text if node is not None else None
    s_value=node.find("Value").text if node is not None else None
    rows.append({
        "date":v_date, "numcode":s_numcode,
        "charcode":s_charcode, "nominal":s_nominal,
        "name":s_name, "value":s_value
    })
df=pd.DataFrame(rows,columns=df_cols)
print(df.head())
