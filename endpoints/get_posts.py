import requests
from endpoints.head_class import Head

class GetPosts(Head):
    len_response = None


    def get_posts(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        self.status = response.status_code
        self.len_response = len(response.json())
        return response


    def check_nuber_posts(self):
        assert self.len_response == 100