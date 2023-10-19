import requests
from endpoints.head_class import Head


class PutPostId(Head):
    body = None
    user_id = None
    title = None
    post_id = None
    ch_title = None
    ch_body = None
    ch_user_id = None
    req_post_id = None

    def put_posts_id(self, create_test_date, post_id):
        title = create_test_date[0]
        body = create_test_date[1]
        user_id = create_test_date[2]
        response = requests.put(
            f'https://jsonplaceholder.typicode.com/posts/{post_id}',
            json={
                "id": post_id,
                "title": title,
                "body": body,
                "userId": user_id
            },
            headers={'Content-type': 'application/json; charset=UTF-8'}
        )

        self.status = response.status_code
        self.body = response.json()['body']
        self.user_id = response.json()['userId']
        self.title = response.json()['title']
        self.post_id = response.json()['id']
        self.ch_title = title
        self.ch_body = body
        self.ch_user_id = user_id
        self.req_post_id = post_id
        return response.json()

    def check_response_body_same_as_change_body(self):
        assert self.body == self.ch_body

    def check_response_title_same_as_change_title(self):
        assert self.title == self.ch_title

    def check_response_userid_same_as_change_userid(self):
        assert self.user_id == self.ch_user_id

    def check_response_post_id_same_as_change_post_id(self):
        assert self.post_id == self.req_post_id

