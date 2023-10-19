def test_create_post(create_test_date, create_post, delete_post):
    test_date = create_post.post_posts(create_test_date)
    create_post.check_response_status_is_ok()
    create_post.check_response_title_same_as_sent_title()
    create_post.check_response_body_same_as_sent_body()
    create_post.check_response_userid_same_as_sent_userid()
    create_post.check_have_id()
    delete_post.delete_post(test_date["id"])
