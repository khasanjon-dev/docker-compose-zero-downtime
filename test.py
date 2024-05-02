import requests

while True:
    try:
        MAX_REQUESTS = input("Enter the number of requests or just ENTER (default=1000):\n")
        if MAX_REQUESTS == '':
            MAX_REQUESTS = 1000
        else:
            MAX_REQUESTS = int(MAX_REQUESTS)
        break
    except:
        print("Must be integer!")

print("Let's started ... !")

data = {}

for i in range(MAX_REQUESTS):
    res = requests.get('http://127.0.0.1/api/v1/news/counter/')
    id_ = res.json()['id']
    container_id = 'container_id: ' + id_
    if data.get(container_id):
        data[container_id] += 1
    else:
        data[container_id] = 1

print("Requests result!")

print(data)
