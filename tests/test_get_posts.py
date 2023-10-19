def test_get_posts(get_posts):
    get_posts.get_posts()
    get_posts.check_response_status_is_ok()
    get_posts.check_nuber_posts()
