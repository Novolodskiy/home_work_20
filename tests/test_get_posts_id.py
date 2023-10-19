def test_get_post_id(create_post, create_test_date, get_post_id, delete_post):
    test_date_post = create_post.post_posts(create_test_date)
    get_post_id.get_post(test_date_post)
    get_post_id.check_response_status_is_ok()
    get_post_id.check_response_body_same_as_post_body()
    get_post_id.check_response_title_same_as_post_title()
    get_post_id.check_response_userid_same_as_post_userid()
    get_post_id.check_response_id_same_as_post_id()
    delete_post.delete_post(test_date_post["id"])
