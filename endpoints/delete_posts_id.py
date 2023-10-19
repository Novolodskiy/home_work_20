import requests
from endpoints.head_class import Head


class DeletePost(Head):

    def delete_post(self, post_id):
        response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
        self.status = response.status_code
        return response
