import urllib.request as request
import json
src="https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"
with request.urlopen(src) as response:
    #data=response.read().decode("utf-8")#取得網站原始碼(HTML、CSS、JS)
    data=json.load(response)#利用json模組處理json格式
    clist=data["records"]#將json的資料放入list
#print(clist)
with open("data.txt","w",encoding="utf-8") as file:   #打開data.txt 檔案操作的模"r","w" 用utf-8的方式解碼
    for country in clist:
        file.write(country['sitename']+"\n")#取得records內sitename的資料