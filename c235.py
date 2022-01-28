import requests
for i in range (1,5000):
    url=f"http://ec2-3-111-8-121.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    r=requests.get(url=url)
    if r.status_code==200:
        print(url)
