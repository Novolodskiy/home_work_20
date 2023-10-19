import pytest
import random
import string
from endpoints.post_posts import PostPosts
from endpoints.delete_posts_id import DeletePost
from endpoints.get_posts import GetPosts
from endpoints.get_posts_id import GetPostId
from endpoints.put_posts_id import PutPostId


def random_str(len_string):
    string_test_date = "".join(random.choice(string.ascii_lowercase) for _ in range(len_string))
    return string_test_date


@pytest.fixture()
def create_post():
    return PostPosts()


@pytest.fixture()
def delete_post():
    return DeletePost()


@pytest.fixture()
def get_posts():
    return GetPosts()


@pytest.fixture()
def get_post_id():
    return GetPostId()

@pytest.fixture()
def put_post():
    return PutPostId()


@pytest.fixture()
def create_test_date():
    title = random_str(5)
    body = random_str(7)
    user_id = random.randint(0, 999)
    return [title, body, user_id]
