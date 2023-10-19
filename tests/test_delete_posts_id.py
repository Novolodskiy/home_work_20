def test_delete_post(create_test_date, create_post, delete_post):
    delete_post.delete_post(create_post.post_posts(create_test_date)['id'])
    delete_post.check_response_status_is_ok()
