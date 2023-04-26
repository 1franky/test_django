import requests
import concurrent.futures

# url = "https://testdjango-production-2df0.up.railway.app/face/getFaces"
url = "http://localhost:3001/face/getFaces"

def send_request():
    files = {
        'ine': open('test.jpg', 'rb')
    }
    response = requests.post(url, files=files)
    print(response.status_code) 



with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    futures = [executor.submit(send_request) for _ in range(100)]


# send_request
