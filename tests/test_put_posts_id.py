def test_put_post_id(create_test_date, create_post, put_post, get_post_id, delete_post):
    test_date = create_post.post_posts(create_test_date)
    put_post.put_posts_id(create_test_date, test_date["id"])
    put_post.check_response_status_is_ok()
    put_post.check_response_body_same_as_change_body()
    put_post.check_response_title_same_as_change_title()
    put_post.check_response_post_id_same_as_change_post_id()
    put_post.check_response_userid_same_as_change_userid()
    delete_post.delete_post(test_date["id"])