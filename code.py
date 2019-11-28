import json
import datetime

#r = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
with open('D:\\new_image.json') as json_file:
    data = json.load(json_file)
    for p in data:
        #print(p['creationTimestamp'].split("T")[0])
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
        print(date_time_obj)
        print(p['name'].split("-")[0])
        print(p['name'].split("-")[1])
        
        
