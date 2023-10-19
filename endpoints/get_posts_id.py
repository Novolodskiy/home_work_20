import requests
from endpoints.head_class import Head


class GetPostId(Head):
    body = None
    user_id = None
    title = None
    id = None
    post_title = None
    post_body = None
    post_user_id = None
    post_id = None

    def get_post(self, post_date):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_date["id"]}')
        self.status = response.status_code
        self.body = response.json()['body']
        self.user_id = response.json()['userId']
        self.title = response.json()['title']
        self.id = response.json()['id']
        self.post_title = post_date['title']
        self.post_body = post_date['body']
        self.post_user_id = post_date['user_id']
        self.post_id = post_date['id']
        return response.json()

    def check_response_body_same_as_post_body(self):
        assert self.body == self.post_body

    def check_response_title_same_as_post_title(self):
        assert self.title == self.post_title

    def check_response_userid_same_as_post_userid(self):
        assert self.user_id == self.post_user_id

    def check_response_id_same_as_post_id(self):
        assert self.id == self.post_id
