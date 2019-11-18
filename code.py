import requests

r = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
json_response = r.json()
#print (json_response)

#For processing last lines
a=json_response[len(json_response)-2]
b=json_response[len(json_response)-1]
lista = [k for k in a.values()]
listb = [k for k in b.values()]
ida=print(lista[0])
idb=print(listb[0])
da=print(lista[1])
db=print(listb[1])


#Net Calc
data=1
for k in json_response:
    prem=-1
    listf = [m for m in k]
    #print(k)
    for j in listf:
        prem+=1
        if(j== 'email'):
            listq = [k for k in k.values()]
            data1=listq[prem-2]
            proc=((data1-data)/data)*100
            data=data1
            print(proc)
