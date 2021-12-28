import urllib.request
import json
from six.moves import urllib
import pandas as pd
def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

urlData = "http://webservies.be/eurosong/Votes"
jsonData = getResponse(urlData)
# print the state id and state name corresponding
list_id=[]
for i in jsonData:
    
    songid=f'{i["songID"]}'
  
    list_id.append(songid)
    

   

list_points=[]
for i in jsonData:
    points=f'{i["points"]}'

    list_points.append(int(points))

urlData = "http://webservies.be/eurosong/Songs"
jsonData = getResponse(urlData)
list_org_id=[]
for i in jsonData:
    org_id=f'{i["id"]}'

    list_org_id.append(int(org_id))

list_title=[]
for i in jsonData:
    title=f'{i["title"]}'

    list_title.append(str(title))



  

df = pd.DataFrame(list(zip(list_id, list_points)),
               columns =['songID', 'points'])



df2 = df.groupby('songID')['points'].sum().sort_values( ascending=False)





print(df2)
