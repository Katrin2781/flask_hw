import requests


response = requests.post(
    'http://127.0.0.1:5000/hello/w',
    params={
        'k1':'v1',
        'k2':'v2',
            },
    json={
        'hi':'world'
    },
    headers={
        'token':'xxxx-xxxxx-xxx-xxx'
    }



                         )
print(response.status_code)
print(response.json())

