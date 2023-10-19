import requests


class PostPosts:
    body = None
    user_id = None
    title = None
    id = None
    req_title = None
    req_body = None
    req_user_id = None
    status = None

    def post_posts(self, create_test_date):
        title = create_test_date[0]
        body = create_test_date[1]
        user_id = create_test_date[2]
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json={
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
        self.id = response.json()['id']
        self.req_title = title
        self.req_body = body
        self.req_user_id = user_id
        return response.json()

    def check_response_body_same_as_sent_body(self):
        assert self.body == self.req_body

    def check_response_title_same_as_sent_title(self):
        assert self.title == self.req_title

    def check_response_userid_same_as_sent_userid(self):
        assert self.user_id == self.req_user_id

    def check_have_id(self):
        assert self.id > 0

    def check_response_status_is_ok(self):
        assert self.status == 201
