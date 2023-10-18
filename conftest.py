import pytest
import random
import requests


@pytest.fixture()
def create_post():
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json={
            "title": f'{random.choice}',
            "body": 'bar',
            "userId": 1
        },
        headers={'Content-type': 'application/json; charset=UTF-8'}
    )
    return
