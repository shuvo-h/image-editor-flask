import requests

def get_all_users(allQueryParams):
    print(allQueryParams)
    response = requests.get('https://jsonplaceholder.typicode.com/users',params=allQueryParams)
    return response.json()
