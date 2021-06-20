key=input()
if key != "284":
    exit()
import requests, bs4, json
htmlFile = requests.get("Y URL")
objSoup = bs4.BeautifulSoup(htmlFile.text, "lxml")
headline_news = objSoup.find_all("a", class_="Fz(16px) LineClamp(1,20px) Fw(700) Td(n) Td(u):h C(#324fe1) V(h) active_V(v)")
print("焦點新聞：")
for h in headline_news:
    print(h.text)
print()
url='https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-069?Authorization=' + 'ENTER YOUR API KEY HERE' + '&format=JSON&locationName=%E6%9D%BF%E6%A9%8B%E5%8D%80&elementName=Wx,T,PoP6h'
htmlfile = requests.get(url)
data = json.loads(htmlfile.text)
print(data["records"]["locations"][0]["location"][0]["locationName"],"天氣預報")
print(" "*26,"氣溫 降雨機率")
for n in range(24):
    startTime = data["records"]["locations"][0]["location"][0]["weatherElement"][0]["time"][n]["startTime"][5:16]
    endTime = data["records"]["locations"][0]["location"][0]["weatherElement"][0]["time"][n]["endTime"][5:16]
    value = data["records"]["locations"][0]["location"][0]["weatherElement"][0]["time"][n]["elementValue"][0]["value"]
    value2 = data["records"]["locations"][0]["location"][0]["weatherElement"][1]["time"][n]["elementValue"][0]["value"]
    n //= 2 # 因為降雨機率只有6小時的資料，故索引整除2
    value3 = data["records"]["locations"][0]["location"][0]["weatherElement"][2]["time"][n]["elementValue"][0]["value"]
    #print(f"{startTime} ~ {endTime} 氣溫{value2:2s}度 降雨機率{value3:>3s}% {value}")
    print(f"{startTime} ~ {endTime}  {value2:2s}度 {value3:>3s}%   {value}")
n=input()
